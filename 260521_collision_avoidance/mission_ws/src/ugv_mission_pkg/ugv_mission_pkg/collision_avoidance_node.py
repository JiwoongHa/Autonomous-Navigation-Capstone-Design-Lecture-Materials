#!/usr/bin/env python3
"""
Simple Arc Planner Node

Implements a dynamic window approach (DWA) style arc-based path planner.
The planner generates multiple arc trajectories and selects the best one
based on collision avoidance and goal alignment.

[CHANGED]       Subscriber topics updated to /ugv/state/...

[OPT 1]         Arc trajectories pre-computed at init (vectorized NumPy, cumsum).
[OPT 2]         Collision check fully vectorized across all arcs simultaneously.
[OPT 3]         Score calculation vectorized (no per-arc Python loop).
[OPT 4]         LaserScan nan/inf filtering added in scan_cb.

[FIX VIZ]       scan_cb: planner_enabled 무관하게 LiDAR 수신/헤더 저장 항상 수행.
                control_loop: planner_enabled=False 시에도 시각화만 발행.

[FIX OUTDOOR 1] _target_speed: min_spd 기반 선형 감속 + goal_stop_dist 이내 정지.
[FIX OUTDOOR 2] HOLDING → REVERSING 전환에 holding_loops_required 카운터 도입.
[FIX OUTDOOR 3] scan_cb: lidar_confirm_frames 연속 프레임 확정 방식.
[FIX OUTDOOR 4] 듀얼 모드 유도 (FREE / AVOIDANCE + 히스테리시스).

[FIX INIT]      goal 미수신 시 현재 헤딩을 목표 방향으로 사용 (직진 + 장애물 회피).
[FIX MODE]      모드 전환 로직을 planner_enabled 체크 앞으로 이동.
[FIX ARC]       ignore_radius / safety_radius_m 원본 동작 검증값으로 복원.

[CLEAN 1]       미사용 임포트(check_mode_flag) 및 미사용 파라미터
                (weights.goal_align, mode.enabled_flag) 제거.
[CLEAN 2]       max_accel 을 하드코딩에서 파라미터(robot.max_accel_m_s2)로 변경.
[CLEAN 3]       _handle_recovery: HOLDING → REVERSING 전환 프레임에서
                즉시 후진 명령이 발행되던 문제 수정.
                return 0.0, 0.0 을 if/else 밖으로 이동하여 전환 프레임 포함
                HOLDING 상태의 모든 프레임에서 정지 명령 반환.
                REVERSING 블록은 다음 루프 호출부터 실행됨.
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
from ugv_mission_pkg.utils.math_utils import pi2pi


class CollisionAvoidanceNode(Node):

    TOPIC_POSITION  = '/ugv/state/position_ned'
    TOPIC_HEADING   = '/ugv/state/heading'
    TOPIC_GOAL      = '/ugv/state/goal_ned'
    TOPIC_LIDAR     = '/lidar/scan'
    TOPIC_MODE_FLAG = '/fmu/out/mode_flag'
    TOPIC_CMD       = '/colA/command'
    TOPIC_DEBUG     = '/colA/debug_markers'

    MODE_FREE      = "FREE"
    MODE_AVOIDANCE = "AVOIDANCE"

    def __init__(self):
        super().__init__('collision_avoidance_node')

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

        # ================================================================
        # Parameters
        # ================================================================
        self.declare_parameters(namespace='', parameters=[

            # ── 시스템 ──────────────────────────────────────────────────
            ('sys.node_period_sec',                  0.05),
            # 제어 루프 주기 (초). 기본 0.05s = 20 Hz.
            # 낮을수록 반응이 빠르지만 CPU 부하 증가.

            # ── 로봇 운동학 ──────────────────────────────────────────────
            ('robot.max_speed_m_s',                  2.0),
            # 최대 전진 속도 (m/s). arc 궤적 시뮬레이션에도 동일하게 적용됨.
            # 높이면 빠르지만 장애물 반응 시간이 짧아짐.

            ('robot.min_speed_m_s',                  0.3),
            # 목표 근처 감속 구간에서의 최소 속도 (m/s).
            # 너무 낮으면 목표 부근에서 기어가고, 너무 높으면 목표를 지나침.

            ('robot.max_yaw_rate_deg_s',             75.0),
            # 최대 회전 속도 (deg/s). arc 후보군의 좌우 최대 꺾임 각도.
            # 높이면 급회전 가능, 낮으면 부드럽지만 좁은 공간 통과 어려움.

            ('robot.safety_radius_m',                0.20),
            # 충돌 판정 반경 (m). arc 경로상의 각 점이 LiDAR 포인트와
            # 이 거리 이내면 해당 arc 를 충돌로 판정.
            # 로봇 실제 반폭 + 여유 마진으로 설정.
            # 너무 크면 통과 가능한 경로도 막힘, 너무 작으면 충돌 위험.
            # ※ 반드시 lidar.ignore_radius_m 보다 작아야 함.

            ('robot.max_accel_m_s2',                 1.0),
            # [CLEAN 2] 가속도 제한 (m/s²). 높이면 빠르게 목표 속도 도달,
            # 낮으면 부드럽게 가속. 이전에는 1.0 으로 하드코딩되어 있었음.

            # ── 경로 계획 ────────────────────────────────────────────────
            ('plan.sim_time_sec',                    3.0),
            # arc 시뮬레이션 시간 (초). 이 시간 동안의 궤적을 미리 계산.
            # 길수록 먼 장애물까지 대비하지만, arc 가 길어져 좁은 공간에서
            # 통과 가능한 경로를 놓칠 수 있음.

            ('plan.dt_sec',                          0.2),
            # arc 시뮬레이션 타임스텝 (초).
            # 작을수록 궤적이 정밀하지만 계산량 증가 (스텝 수 = sim_time / dt).

            ('plan.arc_count',                       20),
            # arc 후보 개수. -max_yaw_rate ~ +max_yaw_rate 를 이 수만큼 등분.
            # 많을수록 세밀한 방향 탐색 가능, 적을수록 계산 빠름.

            ('plan.goal_stop_dist_m',                0.5),
            # 목표 도달 판정 반경 (m). 이 거리 이내면 정지 명령 발행.
            # GPS 오차가 큰 야외에서는 값을 키워야 목표 부근에서 멈춤.

            ('plan.goal_slowdown_dist_m',            5.0),
            # 감속 시작 거리 (m). 이 거리부터 goal_stop_dist 까지
            # max_spd → min_spd 로 선형 감속.

            ('plan.obstacle_free_dist_m',            3.0),
            # FREE ↔ AVOIDANCE 모드 전환 임계 거리 (m).
            # 가장 가까운 장애물이 이 거리보다 가까우면 AVOIDANCE 모드 진입.
            # 멀면 FREE 모드 (atan2 직접 유도).

            ('plan.obstacle_free_hysteresis_m',      0.5),
            # 모드 전환 히스테리시스 (m).
            # AVOIDANCE → FREE 복귀 조건 = obstacle_free_dist + hysteresis.
            # 경계값 근처에서 모드가 빠르게 왔다갔다 하는 현상(chattering) 방지.

            # ── 회수(Recovery) 동작 ──────────────────────────────────────
            ('recovery.front_obstacle_threshold_m',  0.6),
            # 전방 장애물 위험 임계 거리 (m). 전방 ±30° 이내 장애물이
            # 이 거리보다 가까우면 HOLDING 상태로 진입.
            # clear_distance 보다 작거나 같아야 함 (히스테리시스 구조).

            ('recovery.clear_distance_m',            0.6),
            # 전방 장애물 해소 판정 거리 (m). REVERSING 중 전방 장애물이
            # 이 거리 이상 멀어지면 후진을 멈추고 HOLDING 으로 복귀.

            ('recovery.reverse_speed_m_s',          -2.4),
            # 후진 속도 (m/s, 음수). REVERSING 상태에서 발행되는 속도 명령.
            # 절댓값이 클수록 빠르게 후진하지만 제어 안정성 주의.

            ('recovery.holding_duration_sec',        1.0),
            # HOLDING 상태 유지 시간 (초). 이 시간 동안 정지 후 REVERSING 전환.
            # 짧으면 빠르게 후진 시도, 길면 순간 노이즈에 의한 오감지 방지.

            # ── LiDAR 필터 ───────────────────────────────────────────────
            ('lidar.confirm_frames',                 2),
            # 장애물 확정에 필요한 연속 프레임 수.
            # 단일 프레임 노이즈로 인한 허위 장애물 방지.
            # 높이면 안정적이지만 새 장애물 반응이 늦어짐.

            ('lidar.ignore_radius_m',                0.30),
            # LiDAR 자기 반사 무시 반경 (m). 이 거리 이내 포인트는 필터링.
            # 로봇 자체 구조물이나 센서 마운트가 찍히는 것을 방지.
            # ※ 반드시 robot.safety_radius_m 보다 크거나 같아야 함.

            ('debug.enabled',                        True),
            # True 이면 /colA/debug_markers 토픽으로 RViz 시각화 데이터 발행.
            # 운용 시 False 로 설정하면 불필요한 퍼블리싱 제거 가능.
        ])

        self.period       = self.get_parameter('sys.node_period_sec').value
        self.max_spd      = self.get_parameter('robot.max_speed_m_s').value
        self.min_spd      = self.get_parameter('robot.min_speed_m_s').value
        self.max_yaw_rate = radians(self.get_parameter('robot.max_yaw_rate_deg_s').value)
        self.safety_rad   = self.get_parameter('robot.safety_radius_m').value
        self.max_accel    = self.get_parameter('robot.max_accel_m_s2').value  # [CLEAN 2]

        self.sim_time           = self.get_parameter('plan.sim_time_sec').value
        self.sim_dt             = self.get_parameter('plan.dt_sec').value
        self.arc_count          = self.get_parameter('plan.arc_count').value
        self.goal_stop_dist     = self.get_parameter('plan.goal_stop_dist_m').value
        self.goal_slowdown_dist = self.get_parameter('plan.goal_slowdown_dist_m').value
        self.obstacle_free_dist = self.get_parameter('plan.obstacle_free_dist_m').value
        self.obstacle_free_hyst = self.get_parameter('plan.obstacle_free_hysteresis_m').value

        self.front_obstacle_threshold = self.get_parameter('recovery.front_obstacle_threshold_m').value
        self.clear_distance           = self.get_parameter('recovery.clear_distance_m').value
        self.reverse_speed            = self.get_parameter('recovery.reverse_speed_m_s').value

        holding_duration_sec        = self.get_parameter('recovery.holding_duration_sec').value
        self.holding_loops_required = max(1, int(holding_duration_sec / self.period))
        self.lidar_confirm_frames   = self.get_parameter('lidar.confirm_frames').value
        self.ignore_radius          = self.get_parameter('lidar.ignore_radius_m').value

        self.debug = self.get_parameter('debug.enabled').value

        self.candidate_yaw_rates = np.linspace(-self.max_yaw_rate, self.max_yaw_rate, self.arc_count)
        self._arc_traj           = self._precompute_arc_trajectories()
        self._safety_rad_sq      = self.safety_rad ** 2

        # State Variables
        self.curr_pos_ned      = np.zeros(2)
        self.curr_yaw_ned      = 0.0
        self.goal_pos_ned      = np.zeros(2)
        self.goal_received     = False
        self.planner_enabled   = False
        self.last_header       = None

        self.lidar_points_enu      = None
        self.closest_obstacle_dist = 99.9
        self.front_obstacle_dist   = 99.9

        self.guidance_mode     = self.MODE_FREE
        self.recovery_state    = "NORMAL"
        self.holding_loop_cnt  = 0
        self.current_cmd_speed = 0.0

        self._lidar_candidate   = None
        self._lidar_confirm_cnt = 0

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
        self.get_logger().info(f"  Arcs pre-computed        : {A} arcs x {S} steps")
        self.get_logger().info(f"  Safety radius            : {self.safety_rad} m")
        self.get_logger().info(f"  LiDAR ignore radius      : {self.ignore_radius} m")
        self.get_logger().info(f"  Max accel                : {self.max_accel} m/s²")
        self.get_logger().info(f"  Goal stop dist           : {self.goal_stop_dist} m")
        self.get_logger().info(f"  Obstacle-free threshold  : {self.obstacle_free_dist} m "
                               f"(hysteresis +{self.obstacle_free_hyst} m)")
        self.get_logger().info(f"  Holding loops required   : {self.holding_loops_required} "
                               f"({holding_duration_sec:.1f} s)")
        self.get_logger().info(f"  LiDAR confirm frames     : {self.lidar_confirm_frames}")

    # =================================================================
    #                  Pre-computed Trajectories
    # =================================================================
    def _precompute_arc_trajectories(self) -> np.ndarray:
        num_steps = int(self.sim_time / self.sim_dt)
        t         = np.arange(num_steps) * self.sim_dt
        thetas    = self.candidate_yaw_rates[:, np.newaxis] * t[np.newaxis, :]
        dx        = self.max_spd * np.cos(thetas) * self.sim_dt
        dy        = self.max_spd * np.sin(thetas) * self.sim_dt
        return np.stack([np.cumsum(dx, axis=1),
                         np.cumsum(dy, axis=1)], axis=2)  # (A, S, 2)

    # =================================================================
    #                        Callbacks
    # =================================================================
    def pos_cb(self, msg: Point):
        self.curr_pos_ned = np.array([msg.x, msg.y])

    def yaw_cb(self, msg: Float32):
        self.curr_yaw_ned = msg.data

    def goal_cb(self, msg: Point):
        self.goal_pos_ned = np.array([msg.x, msg.y])
        if not self.goal_received:
            self.get_logger().info("Goal received. Switching to goal-directed guidance.")
        self.goal_received = True

    def mode_cb(self, msg: ModeFlag):
        # [CLEAN 1] enable_flag_idx 제거 — modefour 고정 사용
        self.planner_enabled = (msg.modefour > 0.5)

    def scan_cb(self, msg: LaserScan):
        self.last_header = msg.header

        ranges = np.array(msg.ranges, dtype=np.float32)
        angles = np.linspace(msg.angle_min, msg.angle_max, len(ranges))

        max_lookahead = self.max_spd * self.sim_time + 2.0

        valid  = np.isfinite(ranges) & (ranges > self.ignore_radius) & (ranges < max_lookahead)
        ranges = ranges[valid]
        angles = angles[valid]

        if len(ranges) > 0:
            candidate_pts = np.column_stack((ranges * np.cos(angles),
                                             ranges * np.sin(angles)))
            front_mask    = np.abs(angles) < radians(30.0)

            self._lidar_candidate   = (
                candidate_pts,
                float(np.min(ranges)),
                float(np.min(ranges[front_mask])) if np.any(front_mask) else 99.9
            )
            self._lidar_confirm_cnt = min(self._lidar_confirm_cnt + 1,
                                          self.lidar_confirm_frames)

            if self._lidar_confirm_cnt >= self.lidar_confirm_frames:
                pts, closest, front        = self._lidar_candidate
                self.lidar_points_enu      = pts
                self.closest_obstacle_dist = closest
                self.front_obstacle_dist   = front
        else:
            self._lidar_confirm_cnt    = 0
            self._lidar_candidate      = None
            self.lidar_points_enu      = None
            self.closest_obstacle_dist = 99.9
            self.front_obstacle_dist   = 99.9

    # =================================================================
    #                        Main Control Loop
    # =================================================================
    def control_loop(self):
        if self.lidar_points_enu is None:
            return

        # ----------------------------------------------------------
        # 1. Goal Vector
        # ----------------------------------------------------------
        if not self.goal_received:
            goal_yaw_global_ned = self.curr_yaw_ned
            goal_yaw_rel_enu    = 0.0
            dist_to_goal        = None
        else:
            diff_ned     = self.goal_pos_ned - self.curr_pos_ned
            dist_to_goal = float(np.linalg.norm(diff_ned))

            if dist_to_goal < 0.1:
                goal_yaw_global_ned = self.curr_yaw_ned
                goal_yaw_rel_enu    = 0.0
            else:
                goal_yaw_global_ned = atan2(diff_ned[1], diff_ned[0])
                goal_yaw_rel_ned    = pi2pi(goal_yaw_global_ned - self.curr_yaw_ned)
                goal_yaw_rel_enu    = -goal_yaw_rel_ned

        # ----------------------------------------------------------
        # 2. Arc Evaluation (항상 수행)
        # ----------------------------------------------------------
        collisions = self._check_all_collisions()
        scores     = self._score_all_arcs(collisions, goal_yaw_rel_enu)

        best_idx = int(np.argmax(scores))
        if scores[best_idx] == -np.inf:
            best_idx = -1

        # ----------------------------------------------------------
        # 모드 전환 — planner_enabled 와 무관하게 항상 수행
        # ----------------------------------------------------------
        if self.guidance_mode == self.MODE_FREE:
            if self.closest_obstacle_dist < self.obstacle_free_dist:
                self.guidance_mode = self.MODE_AVOIDANCE
                self.get_logger().info(
                    f"[MODE] FREE → AVOIDANCE "
                    f"(closest={self.closest_obstacle_dist:.2f}m < "
                    f"{self.obstacle_free_dist:.2f}m)"
                )
        else:
            exit_threshold = self.obstacle_free_dist + self.obstacle_free_hyst
            if self.closest_obstacle_dist > exit_threshold:
                self.guidance_mode    = self.MODE_FREE
                self.recovery_state   = "NORMAL"
                self.holding_loop_cnt = 0
                self.get_logger().info(
                    f"[MODE] AVOIDANCE → FREE "
                    f"(closest={self.closest_obstacle_dist:.2f}m > {exit_threshold:.2f}m)"
                )

        # ----------------------------------------------------------
        # planner_enabled=False → 시각화만 발행하고 리턴
        # ----------------------------------------------------------
        if not self.planner_enabled:
            if self.debug:
                self._publish_debug(collisions, scores, best_idx,
                                    self.recovery_state, self.guidance_mode)
            return

        # ----------------------------------------------------------
        # 목표 도달 판정 (goal 수신 시에만)
        # ----------------------------------------------------------
        if self.goal_received and dist_to_goal < self.goal_stop_dist:
            self._publish_cmd(0.0, self.curr_yaw_ned)
            if self.debug:
                self._publish_debug(collisions, scores, best_idx,
                                    "GOAL_REACHED", self.guidance_mode)
            return

        # ----------------------------------------------------------
        # 모드별 명령 결정
        # ----------------------------------------------------------
        if self.guidance_mode == self.MODE_FREE:
            cmd_speed, cmd_yaw_absolute_ned = self._compute_free_guidance(
                dist_to_goal, goal_yaw_global_ned)
        else:
            cmd_speed, cmd_yaw_absolute_ned = self._compute_avoidance_guidance(
                dist_to_goal, goal_yaw_rel_enu, best_idx)

        # ----------------------------------------------------------
        # Smooth Acceleration Filter
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

        self._publish_cmd(self.current_cmd_speed, cmd_yaw_absolute_ned)

        if self.debug:
            self._publish_debug(collisions, scores, best_idx,
                                self.recovery_state, self.guidance_mode)

    # =================================================================
    #       FREE MODE
    # =================================================================
    def _compute_free_guidance(self, dist_to_goal, goal_yaw_global_ned: float):
        cmd_speed            = self.max_spd if dist_to_goal is None \
                               else self._target_speed(dist_to_goal)
        cmd_yaw_absolute_ned = pi2pi(goal_yaw_global_ned)
        self.get_logger().info(
            f"[FREE] dist={'N/A' if dist_to_goal is None else f'{dist_to_goal:.2f}m'}  "
            f"hdg={np.degrees(cmd_yaw_absolute_ned):.1f}°  spd={cmd_speed:.2f} m/s",
            throttle_duration_sec=2.0
        )
        return cmd_speed, cmd_yaw_absolute_ned

    # =================================================================
    #       AVOIDANCE MODE
    # =================================================================
    def _compute_avoidance_guidance(self, dist_to_goal, goal_yaw_rel_enu: float,
                                    best_idx: int):
        cmd_speed        = 0.0
        cmd_yaw_rate_enu = 0.0
        spd = self.max_spd if dist_to_goal is None else self._target_speed(dist_to_goal)

        if best_idx != -1:
            if self.front_obstacle_dist >= self.clear_distance:
                self._try_exit_recovery("Path found and front clear")
                cmd_speed        = spd
                cmd_yaw_rate_enu = self.candidate_yaw_rates[best_idx]
            else:
                if self.front_obstacle_dist < self.front_obstacle_threshold:
                    cmd_speed, cmd_yaw_rate_enu = self._handle_recovery(
                        goal_yaw_rel_enu, "Path found but front too close")
                else:
                    self.recovery_state   = "NORMAL"
                    self.holding_loop_cnt = 0
                    cmd_speed        = spd
                    cmd_yaw_rate_enu = self.candidate_yaw_rates[best_idx]
        else:
            if self.front_obstacle_dist < self.front_obstacle_threshold:
                cmd_speed, cmd_yaw_rate_enu = self._handle_recovery(
                    goal_yaw_rel_enu, "All paths blocked")
            else:
                self.recovery_state   = "NORMAL"
                self.holding_loop_cnt = 0
                self.get_logger().warn(
                    f"All paths blocked but front clear "
                    f"({self.front_obstacle_dist:.2f}m). Waiting...",
                    throttle_duration_sec=2.0
                )

        cmd_yaw_absolute_ned = pi2pi(self.curr_yaw_ned + (-cmd_yaw_rate_enu))
        return cmd_speed, cmd_yaw_absolute_ned

    # =================================================================
    #         Vectorized Collision Check / Score
    # =================================================================
    def _check_all_collisions(self) -> np.ndarray:
        pts     = self.lidar_points_enu
        diff    = self._arc_traj[:, :, np.newaxis, :] - pts[np.newaxis, np.newaxis, :, :]
        dist_sq = (diff * diff).sum(axis=-1)
        return dist_sq.min(axis=2).min(axis=1) < self._safety_rad_sq

    def _score_all_arcs(self, collisions: np.ndarray,
                        goal_yaw_rel_enu: float) -> np.ndarray:
        predicted_yaw_ends = self.candidate_yaw_rates * self.sim_time
        raw_diff           = predicted_yaw_ends - goal_yaw_rel_enu
        angle_diffs        = np.abs((raw_diff + pi) % (2 * pi) - pi)
        scores             = 1.0 - angle_diffs / pi
        scores[collisions] = -np.inf
        return scores

    # =================================================================
    #                        Helper Methods
    # =================================================================
    def _target_speed(self, dist_to_goal: float) -> float:
        if dist_to_goal >= self.goal_slowdown_dist:
            return self.max_spd
        ratio = (dist_to_goal - self.goal_stop_dist) / \
                (self.goal_slowdown_dist - self.goal_stop_dist)
        return self.min_spd + float(np.clip(ratio, 0.0, 1.0)) * (self.max_spd - self.min_spd)

    def _publish_cmd(self, speed: float, yaw_absolute_ned: float):
        twist           = Twist()
        twist.linear.x  = float(speed)
        twist.angular.z = float(yaw_absolute_ned)
        self.cmd_pub.publish(twist)

    def _try_exit_recovery(self, reason: str):
        if self.recovery_state != "NORMAL":
            self.get_logger().info(
                f"{reason} ({self.front_obstacle_dist:.2f}m >= "
                f"{self.clear_distance:.2f}m). Resuming normal operation."
            )
        self.recovery_state   = "NORMAL"
        self.holding_loop_cnt = 0

    def _handle_recovery(self, goal_yaw_rel_enu: float, reason: str):
        """
        [CLEAN 3] HOLDING → REVERSING 전환 시 즉시 후진 방지.

        이전: if/else 구조로 REVERSING 전환 프레임에서 else 없이 아래 블록으로
              fall-through 되어 전환 첫 프레임에 즉시 후진 명령 발행.

        이후: return 0.0, 0.0 을 if/else 밖으로 이동.
              HOLDING 상태인 모든 프레임(전환 프레임 포함)에서 정지 명령 반환.
              REVERSING 블록은 다음 루프 호출부터 실행됨.
        """
        if self.recovery_state == "NORMAL":
            self.recovery_state   = "HOLDING"
            self.holding_loop_cnt = 0
            self.get_logger().warn(
                f"{reason} ({self.front_obstacle_dist:.2f}m < "
                f"{self.front_obstacle_threshold:.2f}m). Holding heading.",
                throttle_duration_sec=1.0
            )

        if self.recovery_state == "HOLDING":
            self.holding_loop_cnt += 1
            if self.holding_loop_cnt >= self.holding_loops_required:
                self.recovery_state   = "REVERSING"
                self.holding_loop_cnt = 0
                self.get_logger().warn(
                    f"Holding timeout ({self.holding_loops_required} loops). "
                    f"Switching to REVERSING."
                )
            # [CLEAN 3] 전환 여부와 무관하게 HOLDING 프레임은 항상 정지
            return 0.0, 0.0

        # REVERSING — 위의 return 으로 인해 다음 루프 호출부터 실행됨
        if self.front_obstacle_dist >= self.clear_distance:
            self.get_logger().info(
                f"Front cleared ({self.front_obstacle_dist:.2f}m). Stopping reverse."
            )
            self.recovery_state   = "HOLDING"
            self.holding_loop_cnt = 0
            return 0.0, 0.0

        steering = -np.sign(goal_yaw_rel_enu) * (self.max_yaw_rate * 0.5)
        return self.reverse_speed, steering

    # =================================================================
    #                        Visualization
    # =================================================================
    def _publish_debug(self, collisions: np.ndarray, scores: np.ndarray,
                       best_idx: int, recovery_state: str = "NORMAL",
                       guidance_mode: str = "FREE"):
        if self.last_header is None:
            return

        ma = MarkerArray()

        # 1. Arc 궤적
        for i, traj in enumerate(self._arc_traj):
            m         = Marker()
            m.header  = self.last_header
            m.ns      = "arcs"
            m.id      = i
            m.type    = Marker.LINE_STRIP
            m.action  = Marker.ADD
            m.scale.x = 0.05

            if collisions[i]:
                m.color.r = 1.0; m.color.a = 0.2; m.scale.x = 0.02
            elif i == best_idx:
                m.color.b = 1.0; m.color.a = 1.0; m.scale.x = 0.1
                m.pose.position.z = 0.2
            else:
                m.color.g = 1.0; m.color.a = 0.4

            for pt in traj:
                p = Point(); p.x = float(pt[0]); p.y = float(pt[1])
                m.points.append(p)
            ma.markers.append(m)

        # 2. LiDAR 포인트
        if self.lidar_points_enu is not None and len(self.lidar_points_enu) > 0:
            m_pts         = Marker()
            m_pts.header  = self.last_header
            m_pts.ns      = "valid_points"
            m_pts.id      = 100
            m_pts.type    = Marker.POINTS
            m_pts.action  = Marker.ADD
            m_pts.scale.x = 0.1; m_pts.scale.y = 0.1
            m_pts.color.r = 1.0; m_pts.color.g = 1.0; m_pts.color.a = 0.8

            for pt in self.lidar_points_enu:
                p = Point(); p.x = float(pt[0]); p.y = float(pt[1]); p.z = 0.0
                m_pts.points.append(p)
            ma.markers.append(m_pts)

        # 3. 상태 텍스트
        m_text                 = Marker()
        m_text.header          = self.last_header
        m_text.ns              = "status_text"
        m_text.id              = 200
        m_text.type            = Marker.TEXT_VIEW_FACING
        m_text.action          = Marker.ADD
        m_text.pose.position.z = 2.0
        m_text.scale.z         = 0.5
        m_text.color.a         = 1.0

        if recovery_state == "GOAL_REACHED":
            m_text.color.g = 1.0
            m_text.text    = "GOAL REACHED"

        elif not self.goal_received:
            m_text.color.r = 1.0; m_text.color.g = 1.0
            if recovery_state == "HOLDING":
                m_text.text = (f"NO GOAL | HOLDING "
                               f"({self.holding_loop_cnt}/{self.holding_loops_required})  "
                               f"Front: {self.front_obstacle_dist:.2f}m")
            elif recovery_state == "REVERSING":
                m_text.text = (f"NO GOAL | REVERSING  "
                               f"Front: {self.front_obstacle_dist:.2f}m")
            elif guidance_mode == self.MODE_AVOIDANCE:
                m_text.text = (f"NO GOAL | AVOIDANCE  "
                               f"closest={self.closest_obstacle_dist:.1f}m")
            else:
                m_text.text = (f"NO GOAL | FORWARD MODE  "
                               f"closest={self.closest_obstacle_dist:.1f}m  "
                               f"spd={self.current_cmd_speed:.1f} m/s")

        elif guidance_mode == self.MODE_FREE:
            m_text.color.g = 1.0
            m_text.text    = (f"FREE  closest={self.closest_obstacle_dist:.1f}m  "
                              f"spd={self.current_cmd_speed:.1f} m/s")
        else:
            m_text.color.r = 1.0
            if recovery_state == "HOLDING":
                m_text.text = (f"AVOIDANCE | HOLDING "
                               f"({self.holding_loop_cnt}/{self.holding_loops_required})  "
                               f"Front: {self.front_obstacle_dist:.2f}m")
            elif recovery_state == "REVERSING":
                m_text.text = (f"AVOIDANCE | REVERSING  "
                               f"Front: {self.front_obstacle_dist:.2f}m  "
                               f"spd={self.reverse_speed:.1f} m/s")
            else:
                m_text.color.r = 1.0; m_text.color.g = 0.5
                m_text.text    = (f"AVOIDANCE  closest={self.closest_obstacle_dist:.1f}m  "
                                  f"spd={self.current_cmd_speed:.1f} m/s")

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