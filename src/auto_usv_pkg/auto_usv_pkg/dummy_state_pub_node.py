#!/usr/bin/env python3
"""
dummy_state_pub_node.py — 실내/오프라인 테스트용 가상 상태 발행 노드
─────────────────────────────────────────────────────────────────────
MODE 파라미터로 이동 시나리오 선택:

  static     (기본) 원점 고정, 헤딩 고정, 단일 목표 발행
  moving     /vfh/command 구독 → 위치·헤딩 실시간 적분 (closed-loop 테스트)
  rotating   헤딩이 일정 속도로 회전
  waypoints  경유점 배열 순회, 도달 시 자동 다음 목표
  no_goal    goal 토픽 미발행 → HOLD MODE 테스트

OBSTACLE.MODE 파라미터로 장애물 시나리오 선택:

  none        장애물 없음 (기본)
  fixed       지정 각도·거리·폭의 고정 장애물 (여러 개 가능)
  approaching 정면에서 일정 속도로 접근하는 장애물, 일정 거리 이내 리셋
  wall        정면에 넓은 벽 장애물 (회피 방향 테스트)
  surround    사방에 장애물 배치 (전방 제외 가능) — 탈출 능력 테스트

발행 토픽
  /usv/state/position_ned  geometry_msgs/Point
  /usv/state/heading       std_msgs/Float32
  /usv/state/goal_ned      geometry_msgs/Point   (no_goal 모드 제외)
  /lidar/scan              sensor_msgs/LaserScan  (obstacle.mode != none 이면 항상 발행)

구독 토픽  (moving / waypoints 모드)
  /vfh/command             geometry_msgs/Twist
─────────────────────────────────────────────────────────────────────
파라미터 전체 목록

공통
  mode                    : static | moving | rotating | waypoints | no_goal
  rate_hz                 : 발행 주기 (default: 20.0)
  init.north_m            : 초기 북쪽 위치 (default: 0.0)
  init.east_m             : 초기 동쪽 위치 (default: 0.0)
  init.heading_rad        : 초기 헤딩 (default: 0.0)

이동 시나리오
  goal.north_m            : 목표 북쪽 (default: 5.0)
  goal.east_m             : 목표 동쪽 (default: 0.0)
  rotate.rate_deg_s       : rotating 모드 회전 속도 (default: 10.0)
  waypoints               : 평탄화 경유점 [n0,e0, n1,e1, ...] (default: 사각형)
  waypoint.threshold_m    : 도달 판정 거리 (default: 0.5)

장애물 시나리오
  obstacle.mode           : none | fixed | approaching | wall | surround
  obstacle.fixed          : [angle_deg, dist_m, width_deg, ...] 반복
                            ex) [0.0, 3.0, 10.0,  45.0, 2.0, 8.0]
  obstacle.approach.angle_deg  : 접근 방향 각도 (default: 0.0, 정면)
  obstacle.approach.start_m    : 접근 시작 거리 (default: 8.0)
  obstacle.approach.speed_mps  : 접근 속도 (default: 0.4)
  obstacle.approach.reset_m    : 리셋 트리거 거리 (default: 0.4)
  obstacle.wall.angle_deg      : 벽 방향 (default: 0.0)
  obstacle.wall.dist_m         : 벽까지 거리 (default: 2.5)
  obstacle.wall.width_deg      : 벽 폭 (default: 80.0)
  obstacle.surround.dist_m     : 포위 장애물 거리 (default: 2.0)
  obstacle.surround.gap_deg    : 전방 열린 구간 ±각도 (default: 30.0)

라이다 스캔 설정
  scan.resolution_deg     : 각도 해상도 (default: 1.0)
  scan.range_max_m        : 최대 감지 거리 (default: 12.0)
─────────────────────────────────────────────────────────────────────
"""
from __future__ import annotations
import math
import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.time import Time
from geometry_msgs.msg import Point, Twist
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32


class DummyStatePubNode(Node):

    def __init__(self):
        super().__init__('dummy_state_pub_node')
        self._declare_all_params()

        # ── 공통 ──────────────────────────────────────────────────────────────
        self._mode   = self.get_parameter('mode').value
        rate_hz      = float(self.get_parameter('rate_hz').value)
        self._dt     = 1.0 / rate_hz
        self._north  = float(self.get_parameter('init.north_m').value)
        self._east   = float(self.get_parameter('init.east_m').value)
        self._hdg    = float(self.get_parameter('init.heading_rad').value)

        # ── 이동 시나리오 ────────────────────────────────────────────────────
        self._goal_n     = float(self.get_parameter('goal.north_m').value)
        self._goal_e     = float(self.get_parameter('goal.east_m').value)
        self._rot_rate   = math.radians(float(self.get_parameter('rotate.rate_deg_s').value))
        raw              = list(self.get_parameter('waypoints').value)
        self._wps        = [(raw[i], raw[i+1]) for i in range(0, len(raw)-1, 2)]
        self._wp_thr     = float(self.get_parameter('waypoint.threshold_m').value)
        self._wp_idx     = 0
        self._cmd_speed  = 0.0
        self._cmd_yaw    = self._hdg

        # ── 장애물 시나리오 ──────────────────────────────────────────────────
        self._obs_mode   = self.get_parameter('obstacle.mode').value
        res_deg          = float(self.get_parameter('scan.resolution_deg').value)
        self._scan_res   = math.radians(res_deg)
        self._range_max  = float(self.get_parameter('scan.range_max_m').value)
        self._n_beams    = int(round(360.0 / res_deg))

        # fixed 장애물: [angle_deg, dist_m, width_deg, ...]
        raw_fixed = list(self.get_parameter('obstacle.fixed').value)
        self._fixed_obs = [
            (raw_fixed[i], raw_fixed[i+1], raw_fixed[i+2])
            for i in range(0, len(raw_fixed)-2, 3)
        ]

        # approaching 장애물
        self._app_angle  = math.radians(float(self.get_parameter('obstacle.approach.angle_deg').value))
        self._app_dist   = float(self.get_parameter('obstacle.approach.start_m').value)
        self._app_speed  = float(self.get_parameter('obstacle.approach.speed_mps').value)
        self._app_reset  = float(self.get_parameter('obstacle.approach.reset_m').value)
        self._app_start  = self._app_dist  # 리셋용 원본

        # wall
        self._wall_angle = math.radians(float(self.get_parameter('obstacle.wall.angle_deg').value))
        self._wall_dist  = float(self.get_parameter('obstacle.wall.dist_m').value)
        self._wall_width = math.radians(float(self.get_parameter('obstacle.wall.width_deg').value))

        # surround
        self._sur_dist   = float(self.get_parameter('obstacle.surround.dist_m').value)
        self._sur_gap    = math.radians(float(self.get_parameter('obstacle.surround.gap_deg').value))

        # ── 발행 / 구독 ───────────────────────────────────────────────────────
        self._pub_pos  = self.create_publisher(Point,     '/usv/state/position_ned', 10)
        self._pub_hdg  = self.create_publisher(Float32,   '/usv/state/heading',      10)
        self._pub_goal = self.create_publisher(Point,     '/usv/state/goal_ned',     10)
        self._pub_scan = self.create_publisher(LaserScan, '/lidar/scan',             10)

        if self._mode in ('moving', 'waypoints'):
            self.create_subscription(Twist, '/vfh/command', self._cb_cmd, 10)

        self.create_timer(self._dt, self._loop)
        self._log_start()

    # ── 파라미터 선언 ─────────────────────────────────────────────────────────

    def _declare_all_params(self):
        self.declare_parameters('', [
            ('mode',                         'static'),
            ('rate_hz',                      20.0),
            ('init.north_m',                 0.0),
            ('init.east_m',                  0.0),
            ('init.heading_rad',             0.0),
            ('goal.north_m',                 5.0),
            ('goal.east_m',                  0.0),
            ('rotate.rate_deg_s',            10.0),
            ('waypoints',                    [5.0, 0.0, 5.0, 5.0, 0.0, 5.0, 0.0, 0.0]),
            ('waypoint.threshold_m',         0.5),
            ('obstacle.mode',                'none'),
            ('obstacle.fixed',               [0.0, 3.0, 10.0]),   # angle_deg, dist_m, width_deg
            ('obstacle.approach.angle_deg',  0.0),
            ('obstacle.approach.start_m',    8.0),
            ('obstacle.approach.speed_mps',  0.4),
            ('obstacle.approach.reset_m',    0.4),
            ('obstacle.wall.angle_deg',      0.0),
            ('obstacle.wall.dist_m',         2.5),
            ('obstacle.wall.width_deg',      80.0),
            ('obstacle.surround.dist_m',     2.0),
            ('obstacle.surround.gap_deg',    30.0),
            ('scan.resolution_deg',          1.0),
            ('scan.range_max_m',             12.0),
        ])

    # ── 콜백 ──────────────────────────────────────────────────────────────────

    def _cb_cmd(self, msg: Twist):
        self._cmd_speed = float(msg.linear.x)
        self._cmd_yaw   = float(msg.angular.z)

    # ── 메인 루프 ─────────────────────────────────────────────────────────────

    def _loop(self):
        # 이동 시나리오
        if   self._mode == 'static':    self._step_static()
        elif self._mode == 'moving':    self._step_moving()
        elif self._mode == 'rotating':  self._step_rotating()
        elif self._mode == 'waypoints': self._step_waypoints()
        elif self._mode == 'no_goal':   self._step_no_goal()

        # 장애물 → LaserScan 발행
        self._pub_scan.publish(self._build_scan())

    # ── 이동 시나리오 ─────────────────────────────────────────────────────────

    def _step_static(self):
        self._pub_pos.publish(self._pt(self._north, self._east))
        self._pub_hdg.publish(self._f32(self._hdg))
        self._pub_goal.publish(self._pt(self._goal_n, self._goal_e))

    def _step_moving(self):
        self._hdg    = self._cmd_yaw
        self._north += self._cmd_speed * math.cos(self._hdg) * self._dt
        self._east  += self._cmd_speed * math.sin(self._hdg) * self._dt
        self._pub_pos.publish(self._pt(self._north, self._east))
        self._pub_hdg.publish(self._f32(self._hdg))
        self._pub_goal.publish(self._pt(self._goal_n, self._goal_e))

    def _step_rotating(self):
        self._hdg = self._wrap(self._hdg + self._rot_rate * self._dt)
        self._pub_pos.publish(self._pt(self._north, self._east))
        self._pub_hdg.publish(self._f32(self._hdg))
        self._pub_goal.publish(self._pt(self._goal_n, self._goal_e))

    def _step_waypoints(self):
        if not self._wps:
            return
        gn, ge = self._wps[self._wp_idx]
        if math.hypot(gn - self._north, ge - self._east) < self._wp_thr:
            self._wp_idx = (self._wp_idx + 1) % len(self._wps)
            gn, ge = self._wps[self._wp_idx]
            self.get_logger().info(f'경유점 → {self._wp_idx}: N={gn}, E={ge}')
        self._hdg    = self._cmd_yaw
        self._north += self._cmd_speed * math.cos(self._hdg) * self._dt
        self._east  += self._cmd_speed * math.sin(self._hdg) * self._dt
        self._pub_pos.publish(self._pt(self._north, self._east))
        self._pub_hdg.publish(self._f32(self._hdg))
        self._pub_goal.publish(self._pt(gn, ge))

    def _step_no_goal(self):
        self._pub_pos.publish(self._pt(self._north, self._east))
        self._pub_hdg.publish(self._f32(self._hdg))
        # goal 미발행

    # ── LaserScan 빌더 ────────────────────────────────────────────────────────

    def _build_scan(self) -> LaserScan:
        """현재 obstacle.mode에 맞는 LaserScan 생성."""
        ranges = np.full(self._n_beams, float('inf'))

        if   self._obs_mode == 'fixed':      self._obs_fixed(ranges)
        elif self._obs_mode == 'approaching': self._obs_approaching(ranges)
        elif self._obs_mode == 'wall':        self._obs_wall(ranges)
        elif self._obs_mode == 'surround':    self._obs_surround(ranges)
        # 'none' → 전부 inf 유지

        msg = LaserScan()
        msg.header.stamp    = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'
        msg.angle_min       = -math.pi
        msg.angle_max       =  math.pi - self._scan_res
        msg.angle_increment =  self._scan_res
        msg.range_min       =  0.1
        msg.range_max       =  self._range_max
        msg.ranges          =  ranges.tolist()
        return msg

    def _angle_to_idx(self, angle_rad: float) -> int:
        """각도 → ranges 배열 인덱스 (-π 기준)."""
        a = self._wrap(angle_rad)
        return int(round((a + math.pi) / self._scan_res)) % self._n_beams

    def _fill_beams(self, ranges: np.ndarray, center_rad: float, width_rad: float, dist_m: float):
        """center_rad ± width_rad/2 범위 빔에 dist_m 기록."""
        half = width_rad / 2.0
        n    = max(1, int(round(half / self._scan_res)))
        c    = self._angle_to_idx(center_rad)
        for offset in range(-n, n + 1):
            idx = (c + offset) % self._n_beams
            if dist_m < ranges[idx]:
                ranges[idx] = dist_m

    # ── 장애물 시나리오 함수 ──────────────────────────────────────────────────

    def _obs_fixed(self, ranges: np.ndarray):
        """fixed: self._fixed_obs 의 (angle_deg, dist_m, width_deg) 장애물 삽입."""
        for angle_deg, dist_m, width_deg in self._fixed_obs:
            self._fill_beams(ranges, math.radians(angle_deg),
                             math.radians(width_deg), dist_m)

    def _obs_approaching(self, ranges: np.ndarray):
        """approaching: 매 스텝 거리 감소, reset_m 도달 시 start_m 으로 리셋."""
        self._app_dist -= self._app_speed * self._dt
        if self._app_dist <= self._app_reset:
            self._app_dist = self._app_start
            self.get_logger().info(f'장애물 리셋 → {self._app_start:.1f} m')
        self._fill_beams(ranges, self._app_angle, math.radians(8.0), self._app_dist)

    def _obs_wall(self, ranges: np.ndarray):
        """wall: 지정 방향·거리에 넓은 벽 장애물."""
        self._fill_beams(ranges, self._wall_angle, self._wall_width, self._wall_dist)

    def _obs_surround(self, ranges: np.ndarray):
        """surround: 사방에 장애물. gap_deg 만큼의 전방 구간은 열어 둠."""
        for i in range(self._n_beams):
            angle = -math.pi + i * self._scan_res
            if abs(self._wrap(angle)) > self._sur_gap:
                if self._sur_dist < ranges[i]:
                    ranges[i] = self._sur_dist

    # ── 메시지 헬퍼 ───────────────────────────────────────────────────────────

    @staticmethod
    def _pt(n: float, e: float) -> Point:
        msg = Point(); msg.x, msg.y = n, e; return msg

    @staticmethod
    def _f32(v: float) -> Float32:
        msg = Float32(); msg.data = v; return msg

    @staticmethod
    def _wrap(a: float) -> float:
        return (a + math.pi) % (2.0 * math.pi) - math.pi

    # ── 시작 로그 ─────────────────────────────────────────────────────────────

    def _log_start(self):
        move_info = {
            'static':    f'목표 N={self._goal_n} E={self._goal_e}',
            'moving':    f'목표 N={self._goal_n} E={self._goal_e} | /vfh/command 구독',
            'rotating':  f'회전 {math.degrees(self._rot_rate):.1f} deg/s',
            'waypoints': f'경유점 {len(self._wps)}개: {self._wps}',
            'no_goal':   'goal 미발행 (HOLD MODE 테스트)',
        }.get(self._mode, '?')

        obs_info = {
            'none':       '장애물 없음',
            'fixed':      f'고정 장애물 {len(self._fixed_obs)}개',
            'approaching':f'접근 장애물 — 시작 {self._app_start}m / {self._app_speed}m/s',
            'wall':       f'벽 — {math.degrees(self._wall_angle):.0f}° / {self._wall_dist}m / 폭 {math.degrees(self._wall_width):.0f}°',
            'surround':   f'포위 — 거리 {self._sur_dist}m / 전방 {math.degrees(self._sur_gap):.0f}° 열림',
        }.get(self._obs_mode, '?')

        self.get_logger().info(
            f'DummyStatePubNode\n'
            f'  이동 [{self._mode}]: {move_info}\n'
            f'  장애물 [{self._obs_mode}]: {obs_info}'
        )


# ═══════════════════════════════════════════════════════════════════════════════

def main(args=None):
    rclpy.init(args=args)
    node = DummyStatePubNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
