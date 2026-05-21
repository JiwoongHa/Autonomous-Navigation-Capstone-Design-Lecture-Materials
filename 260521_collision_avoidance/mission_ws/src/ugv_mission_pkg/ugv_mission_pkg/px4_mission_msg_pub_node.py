#!/usr/bin/env python3
"""
PX4 Mission Message Publisher Node

Subscribes to u_ref and psi_ref from multiple mission nodes,
selects the active one based on ModeFlag, and forwards the
commands to PX4 via OffboardControlMode + TrajectorySetpoint.

Architecture:
    Each mission node publishes Twist to its own command topic:
        Twist.linear.x  = u_ref   (forward velocity, m/s)
        Twist.angular.z = psi_ref (absolute yaw, rad, NED)

    This node reads ModeFlag and routes the right command to PX4.

How to add a new mission node:
    1. Add a new entry to MISSION_MODES dict with:
         - 'topic'      : the Twist topic the mission node publishes to
         - 'check_fn'   : lambda that returns True when this mode is active
    2. That's it — no other changes needed.

[CLEAN 1] import numpy as np 제거 — 파일 전체에서 numpy 미사용.
[CLEAN 2] _is_cmd_fresh 메서드 제거 — _timer_cb 에서 신선도 체크를
          인라인으로 직접 처리하고 있어 중복이었음.
          인라인 코드는 lock 으로 보호된 cmd_snapshot 을 사용하므로
          self._cmd 에 직접 접근하는 _is_cmd_fresh 보다 스레드 안전.
"""

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from threading import Lock

from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, ModeFlag
from geometry_msgs.msg import Twist


class Px4MissionMsgPubNode(Node):
    """
    Routes u_ref / psi_ref from multiple mission nodes to PX4
    based on the active ModeFlag.

    To add a new mission:
        Add an entry to MISSION_MODES in __init__().
    """

    TOPIC_OFFBOARD_CONTROL_MODE = '/fmu/in/offboard_control_mode'
    TOPIC_TRAJECTORY_SETPOINT   = '/fmu/in/trajectory_setpoint'
    TOPIC_MODE_FLAG             = '/fmu/out/mode_flag'

    def __init__(self):
        super().__init__('px4_mission_msg_pub_node')

        self.declare_parameter('timer_period_sec', 0.02)   # 50 Hz
        self.declare_parameter('cmd_timeout_sec',  0.5)    # stale command threshold

        timer_period     = self.get_parameter('timer_period_sec').value
        self.cmd_timeout = self.get_parameter('cmd_timeout_sec').value

        px4_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self._lock = Lock()

        # ================================================================
        #   MISSION MODE TABLE
        #   'topic'    : Twist topic the mission node publishes u/psi to
        #   'check_fn' : lambda(ModeFlag) → bool  (True = this mode active)
        #
        #   Priority is determined by ORDER in this dict (top = highest).
        #   Add new missions here — nothing else needs to change.
        # ================================================================
        self.MISSION_MODES = {
            'collision_avoidance': {
                'topic'    : '/colA/command',
                'check_fn' : lambda msg: msg.modefour > 0.5,
            },
            # ── Future missions: uncomment and fill in ──────────────────
            # 'mission_b': {
            #     'topic'    : '/mission_b/command',
            #     'check_fn' : lambda msg: msg.modefive > 0.5,
            # },
            # 'mission_c': {
            #     'topic'    : '/mission_c/command',
            #     'check_fn' : lambda msg: msg.modesix > 0.5,
            # },
        }

        # Per-mission state (auto-initialized from table)
        self._cmd = {}
        for name in self.MISSION_MODES:
            self._cmd[name] = {
                'u_ref'    : 0.0,
                'psi_ref'  : 0.0,
                'received' : False,
                'stamp_ns' : 0,
            }

        self._mode_flags = None

        # --- Publishers ---
        self.offboard_pub = self.create_publisher(
            OffboardControlMode, self.TOPIC_OFFBOARD_CONTROL_MODE, px4_qos)
        self.setpoint_pub = self.create_publisher(
            TrajectorySetpoint, self.TOPIC_TRAJECTORY_SETPOINT, px4_qos)

        # --- Subscribers ---
        self.create_subscription(
            ModeFlag, self.TOPIC_MODE_FLAG, self._mode_flag_cb, px4_qos)

        for name, cfg in self.MISSION_MODES.items():
            def make_cb(mission_name):
                def cb(msg: Twist):
                    with self._lock:
                        self._cmd[mission_name]['u_ref']    = msg.linear.x
                        self._cmd[mission_name]['psi_ref']  = msg.angular.z
                        self._cmd[mission_name]['received'] = True
                        self._cmd[mission_name]['stamp_ns'] = \
                            self.get_clock().now().nanoseconds
                return cb

            self.create_subscription(Twist, cfg['topic'], make_cb(name), sensor_qos)
            self.get_logger().info(f"  Subscribed [{name}] → {cfg['topic']}")

        self.create_timer(timer_period, self._timer_cb)
        self.get_logger().info(
            f"Px4MissionMsgPubNode started at {1.0/timer_period:.0f} Hz."
        )

    # =================================================================
    #                        Callbacks
    # =================================================================
    def _mode_flag_cb(self, msg: ModeFlag):
        with self._lock:
            self._mode_flags = msg

    # =================================================================
    #                        Helper Functions
    # =================================================================
    def _publish_offboard_mode(self, timestamp: int, velocity: bool = True):
        """Publishes OffboardControlMode — velocity control only."""
        msg = OffboardControlMode()
        msg.timestamp    = timestamp
        msg.position     = False
        msg.velocity     = velocity
        msg.acceleration = False
        msg.attitude     = False
        msg.body_rate    = False
        self.offboard_pub.publish(msg)

    def _publish_setpoint(self, timestamp: int, u_ref: float, psi_ref: float):
        """
        Publishes TrajectorySetpoint.
            velocity[0] = u_ref   (forward, NED x)
            velocity[1] = 0.0     (lateral, no sideslip)
            velocity[2] = 0.0     (vertical)
            yaw         = psi_ref (absolute NED yaw)
        """
        msg = TrajectorySetpoint()
        msg.timestamp = timestamp
        msg.position  = [float('nan'), float('nan'), float('nan')]
        msg.velocity  = [float(u_ref), 0.0, 0.0]
        msg.yaw       = float(psi_ref)
        self.setpoint_pub.publish(msg)

    # =================================================================
    #                        Main Timer Loop (50 Hz)
    # =================================================================
    def _timer_cb(self):
        """
        Checks ModeFlag, finds the active mission, and publishes to PX4.
        Priority: order of keys in MISSION_MODES (first match wins).
        """
        with self._lock:
            mode_flags   = self._mode_flags
            cmd_snapshot = {k: dict(v) for k, v in self._cmd.items()}

        if mode_flags is None:
            return

        timestamp      = int(self.get_clock().now().nanoseconds / 1000)
        active_mission = None

        for name, cfg in self.MISSION_MODES.items():
            if cfg['check_fn'](mode_flags):
                active_mission = name
                break

        if active_mission is None:
            return

        state = cmd_snapshot[active_mission]

        if not state['received']:
            self.get_logger().warn(
                f"[{active_mission}] mode active but no command received yet.",
                throttle_duration_sec=2.0
            )
            return

        # [CLEAN 2] 신선도 체크 인라인 유지 (lock 으로 보호된 snapshot 사용)
        # _is_cmd_fresh 는 self._cmd 에 직접 접근하여 스레드 안전하지 않아 제거
        age = (self.get_clock().now().nanoseconds - state['stamp_ns']) / 1e9
        if age > self.cmd_timeout:
            self.get_logger().warn(
                f"[{active_mission}] command stale ({age:.2f}s > {self.cmd_timeout}s). "
                f"Skipping publish.",
                throttle_duration_sec=1.0
            )
            return

        u_ref   = state['u_ref']
        psi_ref = state['psi_ref']

        self._publish_offboard_mode(timestamp, velocity=True)
        self._publish_setpoint(timestamp, u_ref, psi_ref)

        self.get_logger().info(
            f"[{active_mission}] u={u_ref:.2f} m/s  psi={psi_ref:.3f} rad",
            throttle_duration_sec=2.0
        )


def main(args=None):
    rclpy.init(args=args)
    node = Px4MissionMsgPubNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.')
    except Exception as e:
        node.get_logger().error(f'Executor failed: {e}')
    finally:
        executor.shutdown()
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()