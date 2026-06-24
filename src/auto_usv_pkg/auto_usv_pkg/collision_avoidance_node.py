#!/usr/bin/env python3
"""
collision_avoidance_node.py — ROS 2 arc-based collision avoidance for USV
─────────────────────────────────────────────────────────────────────────────
GOAL MODE  (goal 토픽 수신 시):
  직진 경로 안전 → 목표 방향 직진.
  직진 막힘     → 목표 정렬 점수 최고 아크 선택.
  전 아크 막힘  → 장애물 최소 아크로 저속 진행.

HOLD MODE  (goal 토픽 없음):
  안전 거리 확보 → 제자리 정지.
  장애물 접근   → 무게중심 반대 방향(가장 열린 쪽)으로 저속 이탈.

토픽 구독
  /usv/state/position_ned  geometry_msgs/Point   NED (x=N, y=E)
  /usv/state/heading       std_msgs/Float32      NED 방위각 [rad, CW]
  /usv/state/goal_ned      geometry_msgs/Point   NED 목표  ← 선택
  /lidar/scan              sensor_msgs/LaserScan

토픽 발행
  /vfh/command        geometry_msgs/Twist      linear.x=속도, angular.z=절대 NED 방위각
  /vfh/oa_flag        std_msgs/Bool            회피 중이면 True
  /vfh/debug_markers  visualization_msgs/MarkerArray
                        ns='arcs'      : 빨강=충돌 / 초록=안전 / 파랑굵음=선택
                        ns='obstacles' : 필터된 장애물 (노랑)
                        ns='status'    : 모드·속도·거리 텍스트
─────────────────────────────────────────────────────────────────────────────
"""
from __future__ import annotations
import math
import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from geometry_msgs.msg import Point, Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool, Float32
from visualization_msgs.msg import Marker, MarkerArray


# ═══════════════════════════════════════════════════════════════════════════════
#  수학 / 계획 (순수 함수)
# ═══════════════════════════════════════════════════════════════════════════════

def pi2pi(a: float) -> float:
    """각도를 (−π, π] 로 정규화."""
    return (a + math.pi) % (2.0 * math.pi) - math.pi


def ned_yaw(heading: float, rate_enu: float) -> float:
    """ENU 요각 오프셋 → 절대 NED 방위각 (ENU CCW = NED 음방향). 호출부는 rate×T 를 넘김."""
    return pi2pi(heading - rate_enu)



def scan_to_points(
    msg: LaserScan,
    ignore_r: float,
    max_r: float,
    cluster_min: int,
    cluster_gap: float,
) -> np.ndarray:
    """
    LaserScan → 2D 바디프레임 장애물 배열 (N, 2).
    x=전방, y=좌측, CCW 양수 (로컬 ENU).  클러스터 필터로 노이즈 제거.
    """
    n      = len(msg.ranges)
    angles = np.linspace(msg.angle_min, msg.angle_max, n)
    ranges = np.asarray(msg.ranges, dtype=np.float64)

    valid  = np.isfinite(ranges) & (ranges > ignore_r) & (ranges < max_r)
    angles, ranges = angles[valid], ranges[valid]
    if len(ranges) == 0:
        return np.empty((0, 2))

    xy    = np.column_stack([ranges * np.cos(angles), ranges * np.sin(angles)])
    keep  = np.zeros(len(ranges), dtype=bool)
    gaps  = np.linalg.norm(np.diff(xy, axis=0), axis=1) if len(xy) > 1 else np.array([])
    start = 0
    for i in range(len(gaps) + 1):
        if (i == len(gaps)) or (gaps[i] > cluster_gap):
            if (i - start + 1) >= cluster_min:
                keep[start : i + 1] = True
            start = i + 1
    return xy[keep]


def simulate_arc_bank(speed: float, rates: np.ndarray, T: float, dt: float) -> np.ndarray:
    """
    모든 yaw rate 의 등속 원호 궤적을 한 번에 생성 (벡터화). 반환: (R, K, 2).
    기존 simulate_arc 루프와 수치적으로 동일. 궤적 위치는 speed 에 선형 비례하므로
    speed=1 단위뱅크를 한 번 만들고 런타임엔 speed 스칼라만 곱해 재사용.
    """
    steps = max(1, int(T / dt))
    j = np.arange(steps)                              # (K,)
    theta = rates[:, None] * (dt * j)[None, :]        # (R, K)
    dx = speed * dt * np.cos(theta)
    dy = speed * dt * np.sin(theta)
    return np.stack([np.cumsum(dx, axis=1), np.cumsum(dy, axis=1)], axis=2)


def arc_collides(traj: np.ndarray, obs: np.ndarray, r: float) -> bool:
    """궤적 상의 임의 점이 장애물 r 이내에 있으면 True (직진 경로 체크용)."""
    if len(obs) == 0 or len(traj) == 0:
        return False
    d = traj[:, None, :] - obs[None, :, :]
    return bool(np.any(np.einsum('kmd,kmd->km', d, d) < r * r))


def straight_path(dist: float, rel_yaw: float, max_spd: float, sim_t: float, safety_r: float) -> np.ndarray:
    """충돌 체크용 직진 경로 샘플링 (바디프레임)."""
    path_len = min(dist, max(max_spd * sim_t, safety_r))
    steps    = max(2, int(path_len / 0.2) + 1)
    s        = np.linspace(0.0, path_len, steps)
    return np.column_stack([s * math.cos(rel_yaw), s * math.sin(rel_yaw)])


def clearance_per_arc(trajs: np.ndarray, obs: np.ndarray) -> np.ndarray:
    """각 아크(R개)의 궤적-장애물 최소 거리 (R,). 장애물 없으면 inf."""
    R = trajs.shape[0]
    dmins = np.full(R, np.inf)
    if len(obs):
        for i in range(R):
            d = trajs[i][:, None, :] - obs[None, :, :]
            dmins[i] = math.sqrt(float(np.einsum('kmd,kmd->km', d, d).min()))
    return dmins


def evaluate_bank(
    trajs: np.ndarray,
    rates: np.ndarray,
    goal_yaw_rel_enu: float,
    obs: np.ndarray,
    T: float,
    r: float,
    w_clear: float,
    clear_scale: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    아크뱅크 평가 (dict 미할당, 전부 ndarray).
    반환: (collision(R,) bool, scores(R,), dmins(R,))
      score = 목표정렬(rate·T 지평, 명령과 동일) + w_clear·(안전반경 초과 여유 정규화)
      충돌 아크의 score = -inf. 동률은 직진(|rate| 작은 쪽) 미세 선호.
    """
    dmins = clearance_per_arc(trajs, obs)
    collision = dmins < r
    head_change = rates * T
    align = np.abs((head_change - goal_yaw_rel_enu + np.pi) % (2.0 * np.pi) - np.pi) / np.pi
    scores = (1.0 - align) + w_clear * np.clip((dmins - r) / clear_scale, 0.0, 1.0)
    scores = scores - 1e-6 * np.abs(rates)            # 동률 tiebreak → 직진 선호
    scores[collision] = -np.inf
    return collision, scores, dmins


def select_best(scores: np.ndarray, collision: np.ndarray, prev_idx: int, margin: float) -> int:
    """
    충돌 없는 아크 중 최고 score 인덱스 (히스테리시스). 전부 막히면 -1.
    직전 선택이 유효하면 새 후보가 margin 이상 더 좋을 때만 전환(떨림 억제).
    """
    valid = ~collision
    if not valid.any():
        return -1
    best = int(np.argmax(np.where(valid, scores, -np.inf)))
    if 0 <= prev_idx < len(scores) and valid[prev_idx]:
        if scores[best] <= scores[prev_idx] + margin:
            return prev_idx
    return best


# ═══════════════════════════════════════════════════════════════════════════════
#  디버그 마커 빌더 (순수 함수, MarkerArray 반환)
# ═══════════════════════════════════════════════════════════════════════════════

def _marker(header, ns: str, mid: int, mtype: int) -> Marker:
    m = Marker()
    m.header, m.ns, m.id, m.type, m.action = header, ns, mid, mtype, Marker.ADD
    return m


def build_arc_markers(trajs: np.ndarray, collision: np.ndarray, best_idx: int, header) -> MarkerArray:
    """빨강=충돌 / 초록=안전 / 파랑굵음=선택 아크 라인 마커."""
    ma = MarkerArray()
    for i in range(trajs.shape[0]):
        m = _marker(header, 'arcs', i, Marker.LINE_STRIP)
        if collision[i]:
            m.color.r, m.color.a, m.scale.x = 1.0, 0.25, 0.02
        elif i == best_idx:
            m.color.b, m.color.a, m.scale.x = 1.0, 1.0,  0.10
            m.pose.position.z = 0.1
        else:
            m.color.g, m.color.a, m.scale.x = 1.0, 0.45, 0.05
        for xy in trajs[i]:
            pt = Point(); pt.x, pt.y = float(xy[0]), float(xy[1])
            m.points.append(pt)
        ma.markers.append(m)
    return ma


def build_direct_marker(path: np.ndarray, header) -> MarkerArray:
    """직진 경로 파랑 라인 마커."""
    ma = MarkerArray()
    m  = _marker(header, 'arcs', 0, Marker.LINE_STRIP)
    m.color.b, m.color.a, m.scale.x = 1.0, 1.0, 0.10
    for xy in path:
        pt = Point(); pt.x, pt.y = float(xy[0]), float(xy[1])
        m.points.append(pt)
    ma.markers.append(m)
    return ma


def build_obstacle_markers(obs: np.ndarray, header) -> MarkerArray:
    """필터된 장애물 포인트 노랑 마커."""
    ma = MarkerArray()
    if len(obs) == 0:
        return ma
    m = _marker(header, 'obstacles', 100, Marker.POINTS)
    m.scale.x = m.scale.y = 0.10
    m.color.r, m.color.g, m.color.a = 1.0, 1.0, 0.9
    for xy in obs:
        pt = Point(); pt.x, pt.y = float(xy[0]), float(xy[1])
        m.points.append(pt)
    ma.markers.append(m)
    return ma


def build_status_marker(
    mode: str, speed: float, dist_to_goal: float, closest: float,
    has_goal: bool, header,
) -> MarkerArray:
    """모드·속도·거리 텍스트 마커."""
    ma = MarkerArray()
    m  = _marker(header, 'status', 200, Marker.TEXT_VIEW_FACING)
    m.pose.position.z = 2.0
    m.scale.z = 0.4
    m.color.r = m.color.g = m.color.b = m.color.a = 1.0
    goal_str  = f'{dist_to_goal:.1f} m' if has_goal else 'None'
    m.text = (
        f'[{mode}]\n'
        f'velocity: {speed:.2f} m/s\n'
        f'dist_goal: {goal_str}\n'
        f'min_obs: {closest:.2f} m'
    )
    ma.markers.append(m)
    return ma


def publish_all(pub, *marker_arrays) -> None:
    """여러 MarkerArray를 하나로 합쳐 발행."""
    combined = MarkerArray()
    for ma in marker_arrays:
        combined.markers.extend(ma.markers)
    pub.publish(combined)


# ═══════════════════════════════════════════════════════════════════════════════
#  노드 (조율 역할만 담당)
# ═══════════════════════════════════════════════════════════════════════════════

class CollisionAvoidanceNode(Node):

    def __init__(self):
        super().__init__('collision_avoidance_node')
        self._declare_params()
        self._load_params()

        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
        )

        self._rates = np.linspace(-self.MAX_YAW_RATE, self.MAX_YAW_RATE, self.ARC_COUNT)
        # 단위속도 아크뱅크 1회 precompute (궤적은 speed 에 선형 비례 → 런타임 스칼라 곱)
        self._arc_unit = simulate_arc_bank(1.0, self._rates, self.SIM_T, self.SIM_DT)  # (R,K,2)
        self._prev_idx = -1   # 히스테리시스용 직전 선택 아크 인덱스

        self._pos_ned:   np.ndarray | None = None
        self._heading:   float | None      = None
        self._goal_ned:  np.ndarray | None = None
        self._obs:       np.ndarray        = np.empty((0, 2))
        self._scan_hdr                     = None
        # 마지막 수신 시각 [ns] — staleness(센서 끊김) 감지용
        self._t_pos:     int | None        = None
        self._t_heading: int | None        = None
        self._t_scan:    int | None        = None

        self.create_subscription(Point,     '/usv/state/position_ned', self._cb_pos,     sensor_qos)
        self.create_subscription(Float32,   '/usv/state/heading',      self._cb_heading, sensor_qos)
        self.create_subscription(Point,     '/usv/state/goal_ned',     self._cb_goal,    sensor_qos)
        self.create_subscription(LaserScan, '/lidar/scan',             self._cb_scan,    sensor_qos)

        self._pub_cmd   = self.create_publisher(Twist,       '/vfh/command',       10)
        self._pub_flag  = self.create_publisher(Bool,        '/vfh/oa_flag',       10)
        self._pub_debug = self.create_publisher(MarkerArray, '/vfh/debug_markers_', 10)

        self.create_timer(1.0 / self.RATE_HZ, self._loop)
        self.get_logger().info('CollisionAvoidanceNode Ready!!')

    # ── 파라미터 선언 / 로드 ──────────────────────────────────────────────────

    def _declare_params(self):
        self.declare_parameters('', [
            ('sys.rate_hz',               20.0),
            ('sys.sensor_timeout_sec',     0.5),   # 센서 입력 stale 판정 시간 [s]
            ('robot.max_speed_m_s',        2.5),
            ('robot.max_yaw_rate_deg_s',  90.0),
            ('robot.safety_radius_m',      0.60),
            ('plan.sim_time_sec',          3.0),
            ('plan.sim_steps',            15),
            ('plan.arc_count',            21),
            ('plan.hysteresis_margin',     0.10),  # 직전 선택 전환 임계(클수록 떨림↓·반응↓)
            ('plan.clearance_weight',      0.30),  # 점수 내 여유(clearance) 가중치
            ('plan.clearance_scale_m',     3.0),   # 여유 정규화 스케일 [m]
            ('hold.clear_m',               1.0),
            ('hold.escape_speed_m_s',      0.6),
            ('lidar.ignore_radius_m',      0.6),
            ('lidar.cluster_min_points',   3),
            ('lidar.cluster_max_gap_m',    0.45),
        ])

    def _load_params(self):
        g = lambda name: self.get_parameter(name).value
        self.RATE_HZ        = float(g('sys.rate_hz'))
        self.SENSOR_TIMEOUT = float(g('sys.sensor_timeout_sec'))
        self.MAX_SPEED    = float(g('robot.max_speed_m_s'))
        self.MAX_YAW_RATE = math.radians(float(g('robot.max_yaw_rate_deg_s')))
        self.SAFETY_R     = float(g('robot.safety_radius_m'))
        self.SIM_T        = float(g('plan.sim_time_sec'))
        self.SIM_DT       = self.SIM_T / int(g('plan.sim_steps'))
        self.ARC_COUNT    = int(g('plan.arc_count'))
        self.HYST_MARGIN  = float(g('plan.hysteresis_margin'))
        self.CLEAR_W      = float(g('plan.clearance_weight'))
        self.CLEAR_SCALE  = float(g('plan.clearance_scale_m'))
        self.HOLD_CLEAR   = float(g('hold.clear_m'))
        self.ESCAPE_SPEED = float(g('hold.escape_speed_m_s'))
        self.IGNORE_R     = float(g('lidar.ignore_radius_m'))
        self.MAX_RANGE    = self.MAX_SPEED * self.SIM_T + 2.0
        self.CLUSTER_MIN  = int(g('lidar.cluster_min_points'))
        self.CLUSTER_GAP  = float(g('lidar.cluster_max_gap_m'))

    # ── 콜백 ──────────────────────────────────────────────────────────────────

    def _cb_pos(self,     msg: Point):    self._pos_ned = np.array([msg.x, msg.y]); self._t_pos = self._now_ns()
    def _cb_heading(self, msg: Float32):  self._heading = float(msg.data);          self._t_heading = self._now_ns()
    def _cb_goal(self,    msg: Point):    self._goal_ned = np.array([msg.x, msg.y])

    def _now_ns(self) -> int:
        return self.get_clock().now().nanoseconds

    def _cb_scan(self, msg: LaserScan):
        self._scan_hdr = msg.header
        self._t_scan = self._now_ns()
        self._obs = scan_to_points(msg, self.IGNORE_R, self.MAX_RANGE, self.CLUSTER_MIN, self.CLUSTER_GAP)

    # ── 메인 제어 루프 ─────────────────────────────────────────────────────────

    def _stale(self, t: int | None, now: int) -> bool:
        """수신 시각이 없거나 timeout 초과면 True."""
        return t is None or (now - t) * 1e-9 > self.SENSOR_TIMEOUT

    def _loop(self):
        if self._pos_ned is None or self._heading is None:
            return

        # ── 센서 staleness 페일세이프 ─────────────────────────────────────────
        # 위치·헤딩·스캔 중 하나라도 끊기면 옛 데이터로 주행하지 않고 정지.
        now = self._now_ns()
        if (self._stale(self._t_pos, now) or self._stale(self._t_heading, now)
                or self._stale(self._t_scan, now)):
            self._pub_cmd.publish(self._twist(0.0, self._heading))
            self._pub_flag.publish(self._bool(False))
            self.get_logger().warn('센서 입력 stale — 정지 유지.', throttle_duration_sec=2.0)
            return

        obs     = self._obs
        hdr     = self._scan_hdr
        dbg     = hdr is not None and self._pub_debug.get_subscription_count() > 0
        closest = float(np.min(np.linalg.norm(obs, axis=1))) if len(obs) else math.inf

        # ── HOLD MODE ─────────────────────────────────────────────────────────
        if self._goal_ned is None:
            # 전방 HOLD_CLEAR 거리 경로가 장애물과 충돌하지 않으면 정지 유지.
            # 옆/뒤 장애물이 가까워도 전방이 열려 있으면 이탈 불필요.
            fwd_path     = straight_path(self.HOLD_CLEAR, 0.0, self.ESCAPE_SPEED, self.SIM_T, self.SAFETY_R)
            forward_clear = not arc_collides(fwd_path, obs, self.SAFETY_R)
            if forward_clear:
                self._prev_idx = -1
                self._pub_cmd.publish(self._twist(0.0, self._heading))
                self._pub_flag.publish(self._bool(False))
                if dbg:
                    publish_all(self._pub_debug,
                                build_obstacle_markers(obs, hdr),
                                build_status_marker('HOLD — Stop', 0.0, 0.0, closest, False, hdr))
            else:
                centroid   = np.mean(obs, axis=0)
                escape_enu = math.atan2(-centroid[1], -centroid[0])
                trajs      = self.ESCAPE_SPEED * self._arc_unit
                collision, scores, dmins = evaluate_bank(
                    trajs, self._rates, escape_enu, obs,
                    self.SIM_T, self.SAFETY_R, self.CLEAR_W, self.CLEAR_SCALE)
                best_idx = select_best(scores, collision, self._prev_idx, self.HYST_MARGIN)
                self._prev_idx = best_idx
                rate = (float(self._rates[best_idx]) if best_idx != -1
                        else float(self._rates[int(np.argmax(dmins))]))
                self._pub_cmd.publish(self._twist(self.ESCAPE_SPEED, ned_yaw(self._heading, rate * self.SIM_T)))
                self._pub_flag.publish(self._bool(True))
                if dbg:
                    publish_all(self._pub_debug,
                                build_arc_markers(trajs, collision, best_idx, hdr),
                                build_obstacle_markers(obs, hdr),
                                build_status_marker('HOLD — Escape', self.ESCAPE_SPEED, 0.0, closest, False, hdr))
            return

        # ── GOAL MODE ─────────────────────────────────────────────────────────
        diff = self._goal_ned - self._pos_ned
        dist = float(np.linalg.norm(diff))
        spd  = self.MAX_SPEED
        goal_yaw_ned = math.atan2(diff[1], diff[0])
        rel_yaw_enu  = -pi2pi(goal_yaw_ned - self._heading)
        dpath        = straight_path(dist, rel_yaw_enu, self.MAX_SPEED, self.SIM_T, self.SAFETY_R)

        if not arc_collides(dpath, obs, self.SAFETY_R):
            self._prev_idx = -1
            self._pub_cmd.publish(self._twist(spd, ned_yaw(self._heading, rel_yaw_enu)))
            self._pub_flag.publish(self._bool(False))
            if dbg:
                publish_all(self._pub_debug,
                            build_direct_marker(dpath, hdr),
                            build_obstacle_markers(obs, hdr),
                            build_status_marker('Straight', spd, dist, closest, True, hdr))
        else:
            trajs = spd * self._arc_unit
            collision, scores, dmins = evaluate_bank(
                trajs, self._rates, rel_yaw_enu, obs,
                self.SIM_T, self.SAFETY_R, self.CLEAR_W, self.CLEAR_SCALE)
            best_idx = select_best(scores, collision, self._prev_idx, self.HYST_MARGIN)
            self._prev_idx = best_idx
            if best_idx != -1:
                rate, mode = float(self._rates[best_idx]), f'Avoidance (Route {best_idx})'
            else:
                spd *= 0.3
                low_dmins = clearance_per_arc(0.3 * trajs, obs)  # 저속 아크 기준 최다개방
                rate = float(self._rates[int(np.argmax(low_dmins))])
                mode = 'All Route Blocked — low speed'
            self._pub_cmd.publish(self._twist(spd, ned_yaw(self._heading, rate * self.SIM_T)))
            self._pub_flag.publish(self._bool(True))
            if dbg:
                publish_all(self._pub_debug,
                            build_arc_markers(trajs, collision, best_idx, hdr),
                            build_obstacle_markers(obs, hdr),
                            build_status_marker(mode, spd, dist, closest, True, hdr))

    # ── 메시지 생성 (최소화) ───────────────────────────────────────────────────

    @staticmethod
    def _twist(speed: float, yaw_ned: float) -> Twist:
        msg = Twist()
        msg.linear.x, msg.angular.z = float(speed), float(yaw_ned)
        return msg

    @staticmethod
    def _bool(val: bool) -> Bool:
        msg = Bool()
        msg.data = val
        return msg


# ═══════════════════════════════════════════════════════════════════════════════
#  엔트리포인트
# ═══════════════════════════════════════════════════════════════════════════════

def main(args=None):
    rclpy.init(args=args)
    node = CollisionAvoidanceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
