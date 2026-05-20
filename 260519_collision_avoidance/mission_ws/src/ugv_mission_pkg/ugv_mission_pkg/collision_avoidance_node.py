#!/usr/bin/env python3
"""
Simple Arc Planner Node

Implements a dynamic window approach (DWA) style arc-based path planner.
The planner generates multiple arc trajectories and selects the best one
based on collision avoidance and goal alignment.

Key Features:
- Arc trajectory generation with multiple yaw rate candidates
- Collision checking using LiDAR data
- Goal alignment scoring
- NED/ENU coordinate frame conversion handling

[CHANGED] Subscriber topics updated from /usv/state/... to /ugv/state/...
to match the output of coordinate_transformer_node.

[OPT 1] Arc trajectories pre-computed at init (vectorized NumPy, cumsum).
[OPT 2] Collision check fully vectorized across all arcs simultaneously.
[OPT 3] Score calculation vectorized (no per-arc Python loop).
[OPT 4] LaserScan nan/inf filtering added in scan_cb.
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import numpy as np
from math import atan2, pi, radians
from std_msgs.msg import Float32
from px4_msgs.msg import ModeFlag
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point, Twist
from visualization_msgs.msg import MarkerArray, Marker
from ugv_mission_pkg.utils import check_mode_flag
from ugv_mission_pkg.utils.math_utils import pi2pi


class CollisionAvoidanceNode(Node):
    """
    Collision avoidance node based on arc-based path planning (DWA style).

    Generates multiple arc trajectories and selects the best one based on
    collision avoidance and goal alignment.
    """

    # --- Topic Names ---
    TOPIC_POSITION  = '/ugv/state/position_ned'
    TOPIC_HEADING   = '/ugv/state/heading'
    TOPIC_GOAL      = '/ugv/state/goal_ned'
    TOPIC_LIDAR     = '/lidar/scan'
    TOPIC_MODE_FLAG = '/fmu/out/mode_flag'
    TOPIC_CMD       = '/colA/command'
    TOPIC_DEBUG     = '/colA/debug_markers'

    def __init__(self):
        super().__init__('collision_avoidance_node')

        # QoS Profiles
        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        config_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # ================= Parameters =================
        self.declare_parameters(namespace='', parameters=[
            ('sys.node_period_sec',                 0.05),
            ('robot.max_speed_m_s',                 2.0),
            ('robot.max_yaw_rate_deg_s',            75.0),
            ('robot.safety_radius_m',               0.20),
            ('plan.sim_time_sec',                   3.0),
            ('plan.dt_sec',                         0.2),
            ('plan.arc_count',                      20),
            ('recovery.front_obstacle_threshold_m', 0.6),
            ('recovery.clear_distance_m',           0.6),
            ('recovery.reverse_speed_m_s',         -2.4),
            ('weights.goal_align',                  1.0),
            ('mode.enabled_flag',                   2),
            ('debug.enabled',                       True),
        ])

        self.period       = self.get_parameter('sys.node_period_sec').value
        self.max_spd      = self.get_parameter('robot.max_speed_m_s').value
        self.max_yaw_rate = radians(self.get_parameter('robot.max_yaw_rate_deg_s').value)
        self.safety_rad   = self.get_parameter('robot.safety_radius_m').value

        self.sim_time  = self.get_parameter('plan.sim_time_sec').value
        self.sim_dt    = self.get_parameter('plan.dt_sec').value
        self.arc_count = self.get_parameter('plan.arc_count').value

        self.front_obstacle_threshold = self.get_parameter('recovery.front_obstacle_threshold_m').value
        self.clear_distance           = self.get_parameter('recovery.clear_distance_m').value
        self.reverse_speed            = self.get_parameter('recovery.reverse_speed_m_s').value

        self.w_goal          = self.get_parameter('weights.goal_align').value
        self.enable_flag_idx = self.get_parameter('mode.enabled_flag').value
        self.debug           = self.get_parameter('debug.enabled').value

        # Fixed yaw rate candidates
        self.candidate_yaw_rates = np.linspace(-self.max_yaw_rate, self.max_yaw_rate, self.arc_count)

        # [OPT 1] Pre-compute all arc trajectories once at init.
        #
        # candidate_yaw_rates and max_spd are fixed at startup, so the
        # (arc_count, num_steps, 2) array never changes during runtime.
        # This removes arc_count × num_steps Python iterations per 20 Hz loop.
        #
        # Shape: (A=arc_count, S=num_steps, 2)
        self._arc_traj      = self._precompute_arc_trajectories()
        self._safety_rad_sq = self.safety_rad ** 2   # cached to avoid repeated squaring

        # State Variables
        self.curr_pos_ned      = np.zeros(2)
        self.curr_yaw_ned      = 0.0
        self.goal_pos_ned      = np.zeros(2)
        self.planner_enabled   = False
        self.lidar_points_enu  = None
        self.last_header       = None

        self.closest_obstacle_dist = 99.9
        self.front_obstacle_dist   = 99.9

        self.recovery_state    = "NORMAL"  # NORMAL, HOLDING, REVERSING
        self.current_cmd_speed = 0.0
        self.max_accel         = 1.0

        # === Subscribers ===
        self.create_subscription(Point,     self.TOPIC_POSITION,  self.pos_cb,  sensor_qos)
        self.create_subscription(Float32,   self.TOPIC_HEADING,   self.yaw_cb,  sensor_qos)
        self.create_subscription(Point,     self.TOPIC_GOAL,      self.goal_cb, sensor_qos)
        self.create_subscription(LaserScan, self.TOPIC_LIDAR,     self.scan_cb, sensor_qos)
        self.create_subscription(ModeFlag,  self.TOPIC_MODE_FLAG, self.mode_cb, config_qos)

        # === Publishers ===
        self.cmd_pub   = self.create_publisher(Twist,       self.TOPIC_CMD,   10)
        self.debug_pub = self.create_publisher(MarkerArray, self.TOPIC_DEBUG, 10)

        self.create_timer(self.period, self.control_loop)

        A, S, _ = self._arc_traj.shape
        self.get_logger().info("Collision Avoidance Node (NED<->ENU) Started.")
        self.get_logger().info(f"  Arcs pre-computed : {A} arcs x {S} steps")
        self.get_logger().info(f"  Position : {self.TOPIC_POSITION}")
        self.get_logger().info(f"  Heading  : {self.TOPIC_HEADING}")
        self.get_logger().info(f"  Goal     : {self.TOPIC_GOAL}")

    # =================================================================
    #                  [OPT 1] Pre-computed Trajectories
    # =================================================================
    def _precompute_arc_trajectories(self) -> np.ndarray:
        """
        Pre-computes all arc trajectories using vectorized NumPy.

        For each candidate yaw rate w_i and constant forward speed v:
            theta(t) = w_i * t
            x(t)     = cumsum( v * cos(theta) * dt )
            y(t)     = cumsum( v * sin(theta) * dt )

        Returns:
            np.ndarray of shape (arc_count, num_steps, 2)
        """
        num_steps = int(self.sim_time / self.sim_dt)

        # t[j] = j * dt,  shape (S,)
        t = np.arange(num_steps) * self.sim_dt

        # theta[i, j] = yaw_rates[i] * t[j],  shape (A, S)
        thetas = self.candidate_yaw_rates[:, np.newaxis] * t[np.newaxis, :]

        # Incremental displacements, shape (A, S)
        dx = self.max_spd * np.cos(thetas) * self.sim_dt
        dy = self.max_spd * np.sin(thetas) * self.sim_dt

        # Cumulative positions, shape (A, S)
        xs = np.cumsum(dx, axis=1)
        ys = np.cumsum(dy, axis=1)

        return np.stack([xs, ys], axis=2)   # (A, S, 2)

    # =================================================================
    #                        Callbacks
    # =================================================================
    def pos_cb(self, msg: Point):
        """Position callback — from /ugv/state/position_ned (x=N, y=E)."""
        self.curr_pos_ned = np.array([msg.x, msg.y])

    def yaw_cb(self, msg: Float32):
        """Heading callback — from /ugv/state/heading (NED, CW+, rad)."""
        self.curr_yaw_ned = msg.data

    def goal_cb(self, msg: Point):
        """Goal position callback — from /ugv/state/goal_ned (x=N, y=E)."""
        self.goal_pos_ned = np.array([msg.x, msg.y])

    def mode_cb(self, msg: ModeFlag):
        """Mode flag callback — enabled when modefour == 1."""
        self.planner_enabled = (msg.modefour > 0.5)

    def scan_cb(self, msg: LaserScan):
        """Laser scan callback — processes LiDAR data in ENU frame.

        [OPT 4] Added np.isfinite() filter: LaserScan may emit inf/nan for
                out-of-range readings, which would corrupt the collision check.
        """
        if not self.planner_enabled:
            return

        self.last_header = msg.header

        ranges = np.array(msg.ranges, dtype=np.float32)
        angles = np.linspace(msg.angle_min, msg.angle_max, len(ranges))

        ignore_radius = 0.3
        max_lookahead = self.max_spd * self.sim_time + 2.0

        # [OPT 4] isfinite() guards against nan/inf before distance comparisons
        valid  = np.isfinite(ranges) & (ranges > ignore_radius) & (ranges < max_lookahead)
        ranges = ranges[valid]
        angles = angles[valid]

        if len(ranges) > 0:
            self.lidar_points_enu      = np.column_stack((ranges * np.cos(angles),
                                                          ranges * np.sin(angles)))
            self.closest_obstacle_dist = float(np.min(ranges))
            front_mask                 = np.abs(angles) < radians(30.0)
            self.front_obstacle_dist   = float(np.min(ranges[front_mask])) \
                                         if np.any(front_mask) else 99.9
        else:
            self.lidar_points_enu      = None
            self.closest_obstacle_dist = 99.9
            self.front_obstacle_dist   = 99.9

    # =================================================================
    #                        Main Control Loop
    # =================================================================
    def control_loop(self):
        """Main control loop — computes and publishes velocity commands."""
        if not self.planner_enabled or self.lidar_points_enu is None:
            return

        # ----------------------------------------------------------
        # 1. Goal Vector (NED -> ENU)
        # ----------------------------------------------------------
        diff_ned     = self.goal_pos_ned - self.curr_pos_ned
        dist_to_goal = float(np.linalg.norm(diff_ned))

        if dist_to_goal < 0.1:
            goal_yaw_rel_enu = 0.0
        else:
            goal_yaw_global_ned = atan2(diff_ned[1], diff_ned[0])
            goal_yaw_rel_ned    = pi2pi(goal_yaw_global_ned - self.curr_yaw_ned)
            goal_yaw_rel_enu    = -goal_yaw_rel_ned  # NED(CW+) → ENU(CCW+)

        # ----------------------------------------------------------
        # 2. Vectorized Arc Evaluation  [OPT 2, 3]
        # ----------------------------------------------------------
        collisions = self._check_all_collisions()                        # (A,) bool
        scores     = self._score_all_arcs(collisions, goal_yaw_rel_enu)  # (A,) float

        best_idx = int(np.argmax(scores))
        if scores[best_idx] == -np.inf:
            best_idx = -1   # all arcs blocked

        # ----------------------------------------------------------
        # 3. Determine Command
        # ----------------------------------------------------------
        cmd_speed        = 0.0
        cmd_yaw_rate_enu = 0.0

        if best_idx != -1:
            if self.front_obstacle_dist >= self.clear_distance:
                self._try_exit_recovery("Path found and front clear")
                cmd_speed        = self._target_speed(dist_to_goal)
                cmd_yaw_rate_enu = self.candidate_yaw_rates[best_idx]
            else:
                if self.front_obstacle_dist < self.front_obstacle_threshold:
                    cmd_speed, cmd_yaw_rate_enu = self._handle_recovery(
                        goal_yaw_rel_enu, "Path found but front too close")
                else:
                    self.recovery_state = "NORMAL"
                    cmd_speed           = self._target_speed(dist_to_goal)
                    cmd_yaw_rate_enu    = self.candidate_yaw_rates[best_idx]
        else:
            if self.front_obstacle_dist < self.front_obstacle_threshold:
                cmd_speed, cmd_yaw_rate_enu = self._handle_recovery(
                    goal_yaw_rel_enu, "All paths blocked")
            else:
                self.recovery_state = "NORMAL"
                self.get_logger().warn(
                    f"All paths blocked but front clear ({self.front_obstacle_dist:.2f}m). Waiting...",
                    throttle_duration_sec=2.0
                )

        # ----------------------------------------------------------
        # 4. ENU → NED & Absolute Yaw
        # ----------------------------------------------------------
        cmd_yaw_rate_ned     = -cmd_yaw_rate_enu
        cmd_yaw_absolute_ned = pi2pi(self.curr_yaw_ned + cmd_yaw_rate_ned)

        # ----------------------------------------------------------
        # 5. Smooth Acceleration Filter
        # ----------------------------------------------------------
        speed_step = self.max_accel * self.period

        if cmd_speed == 0.0:
            self.current_cmd_speed = 0.0
        elif cmd_speed > 0.0 and cmd_speed > self.current_cmd_speed:
            self.current_cmd_speed = min(cmd_speed, self.current_cmd_speed + speed_step)
        elif cmd_speed < 0.0 and cmd_speed < self.current_cmd_speed:
            self.current_cmd_speed = max(cmd_speed, self.current_cmd_speed - speed_step)
        else:
            self.current_cmd_speed = cmd_speed

        # ----------------------------------------------------------
        # 6. Publish
        # ----------------------------------------------------------
        twist           = Twist()
        twist.linear.x  = float(self.current_cmd_speed)
        twist.angular.z = float(cmd_yaw_absolute_ned)
        self.cmd_pub.publish(twist)

        if self.debug:
            self._publish_debug(collisions, scores, best_idx, self.recovery_state)

    # =================================================================
    #         [OPT 2] Vectorized Collision Check (all arcs at once)
    # =================================================================
    def _check_all_collisions(self) -> np.ndarray:
        """
        Checks collision for ALL arcs simultaneously via NumPy broadcasting.

        Before (sequential):
            for arc in arcs:           # A Python iterations
                for pt in trajectory:  # S Python iterations
                    dist(pt, lidar)    # N ops each
            → A × S Python loop iterations

        After (vectorized):
            (A, S, 1, 2) − (1, 1, N, 2)  →  dist_sq: (A, S, N)
            .min(axis=2).min(axis=1) < r² →  collisions: (A,)
            → 1 Python call, NumPy C-loop handles A×S×N internally

        Returns:
            np.ndarray of shape (A,), dtype bool
        """
        pts = self.lidar_points_enu  # (N, 2)

        # Broadcasting: (A, S, 1, 2) - (1, 1, N, 2) = (A, S, N, 2)
        diff    = self._arc_traj[:, :, np.newaxis, :] - pts[np.newaxis, np.newaxis, :, :]
        dist_sq = (diff * diff).sum(axis=-1)  # (A, S, N)

        # Collision if any step of arc i is within safety_radius of any point
        return dist_sq.min(axis=2).min(axis=1) < self._safety_rad_sq  # (A,)

    # =================================================================
    #         [OPT 3] Vectorized Score Calculation
    # =================================================================
    def _score_all_arcs(self, collisions: np.ndarray, goal_yaw_rel_enu: float) -> np.ndarray:
        """
        Computes scores for ALL arcs simultaneously.

        score_i = 1 - |angle_diff_i| / π   (collision-free arcs)
                = -inf                      (colliding arcs)

        Returns:
            np.ndarray of shape (A,)
        """
        # Predicted final heading for each arc in ENU, shape (A,)
        predicted_yaw_ends = self.candidate_yaw_rates * self.sim_time

        # Vectorized pi2pi: wrap difference to [-π, π]
        raw_diff    = predicted_yaw_ends - goal_yaw_rel_enu
        angle_diffs = np.abs((raw_diff + pi) % (2 * pi) - pi)

        scores             = 1.0 - angle_diffs / pi   # (A,)
        scores[collisions] = -np.inf                  # mask colliding arcs
        return scores

    # =================================================================
    #                        Helper Methods
    # =================================================================
    def _target_speed(self, dist_to_goal: float) -> float:
        """Returns speed scaled by distance when close to goal."""
        if dist_to_goal < 5.0:
            return max(2.0, self.max_spd * (dist_to_goal / 5.0))
        return self.max_spd

    def _try_exit_recovery(self, reason: str):
        """Exits recovery state and logs if state actually changed."""
        if self.recovery_state != "NORMAL":
            self.get_logger().info(
                f"{reason} ({self.front_obstacle_dist:.2f}m >= {self.clear_distance:.2f}m). "
                f"Resuming normal operation."
            )
        self.recovery_state = "NORMAL"

    def _handle_recovery(self, goal_yaw_rel_enu: float, reason: str):
        """
        Manages HOLDING → REVERSING state transitions.
        Returns (cmd_speed, cmd_yaw_rate_enu).
        """
        if self.recovery_state == "NORMAL":
            self.recovery_state = "HOLDING"
            self.get_logger().warn(
                f"{reason} ({self.front_obstacle_dist:.2f}m < "
                f"{self.front_obstacle_threshold:.2f}m). Holding heading.",
                throttle_duration_sec=1.0
            )
        elif self.recovery_state == "HOLDING":
            self.recovery_state = "REVERSING"

        if self.recovery_state == "HOLDING":
            return 0.0, 0.0

        # REVERSING
        if self.front_obstacle_dist >= self.clear_distance:
            self.get_logger().info(
                f"Front cleared ({self.front_obstacle_dist:.2f}m). Stopping reverse."
            )
            self.recovery_state = "HOLDING"
            return 0.0, 0.0

        # 후진 시 목표 방향으로 조향 (무한 루프 탈출)
        steering = -np.sign(goal_yaw_rel_enu) * (self.max_yaw_rate * 0.5)
        return self.reverse_speed, steering

    # =================================================================
    #                        Visualization
    # =================================================================
    def _publish_debug(self, collisions: np.ndarray, scores: np.ndarray,
                       best_idx: int, recovery_state: str = "NORMAL"):
        """Publishes arc trajectories, LiDAR points, and recovery state to RViz."""
        if self.last_header is None:
            return

        ma = MarkerArray()

        # 1. Arc trajectories — use pre-computed _arc_traj directly (no dict overhead)
        for i, traj in enumerate(self._arc_traj):
            m         = Marker()
            m.header  = self.last_header
            m.ns      = "arcs"
            m.id      = i
            m.type    = Marker.LINE_STRIP
            m.action  = Marker.ADD
            m.scale.x = 0.05

            if collisions[i]:
                m.color.r = 1.0; m.color.a = 0.2; m.scale.x = 0.02   # Red
            elif i == best_idx:
                m.color.b = 1.0; m.color.a = 1.0; m.scale.x = 0.1    # Blue (selected)
                m.pose.position.z = 0.2
            else:
                m.color.g = 1.0; m.color.a = 0.4                      # Green (safe)

            for pt in traj:
                p = Point(); p.x = float(pt[0]); p.y = float(pt[1])
                m.points.append(p)

            ma.markers.append(m)

        # 2. LiDAR points
        if self.lidar_points_enu is not None and len(self.lidar_points_enu) > 0:
            m_pts         = Marker()
            m_pts.header  = self.last_header
            m_pts.ns      = "valid_points"
            m_pts.id      = 100
            m_pts.type    = Marker.POINTS
            m_pts.action  = Marker.ADD
            m_pts.scale.x = 0.1
            m_pts.scale.y = 0.1
            m_pts.color.r = 1.0; m_pts.color.g = 1.0; m_pts.color.a = 0.8

            for pt in self.lidar_points_enu:
                p = Point(); p.x = float(pt[0]); p.y = float(pt[1]); p.z = 0.0
                m_pts.points.append(p)

            ma.markers.append(m_pts)

        # 3. Recovery state text
        if recovery_state != "NORMAL":
            m_text                 = Marker()
            m_text.header          = self.last_header
            m_text.ns              = "recovery_state"
            m_text.id              = 200
            m_text.type            = Marker.TEXT_VIEW_FACING
            m_text.action          = Marker.ADD
            m_text.pose.position.z = 2.0
            m_text.scale.z         = 0.5
            m_text.color.r         = 1.0; m_text.color.a = 1.0

            if recovery_state == "HOLDING":
                m_text.text = f"HOLDING (Front: {self.front_obstacle_dist:.2f}m)"
            elif recovery_state == "REVERSING":
                m_text.text = (f"REVERSING (Front: {self.front_obstacle_dist:.2f}m, "
                               f"Speed: {self.reverse_speed:.2f} m/s)")

            ma.markers.append(m_text)

        self.debug_pub.publish(ma)


def main(args=None):
    rclpy.init(args=args)
    node = CollisionAvoidanceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()