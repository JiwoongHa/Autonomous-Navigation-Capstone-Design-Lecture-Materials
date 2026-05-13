#!/usr/bin/env python3
"""
UGV Obstacle Avoidance Node (LiDAR 기반 좌/우 회피)

장애물이 UGV 기준 오른쪽에 있으면 좌회전 (steering_pwm=1100),
왼쪽에 있으면 우회전 (steering_pwm=1900),
장애물 없으면 직진 (steering_pwm=1500).
motor_pwm은 항상 1500 (정지).

파라미터 실시간 변경 지원:
    ros2 param set /obstacle_avoidance_node detection.obstacle_distance_m 1.0
    ros2 param set /obstacle_avoidance_node detection.front_angle_deg 60.0
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from rcl_interfaces.msg import SetParametersResult
import numpy as np
from math import radians, cos, sin

from sensor_msgs.msg import LaserScan
from px4_msgs.msg import ActuatorCommand
from visualization_msgs.msg import MarkerArray, Marker
from geometry_msgs.msg import Point


# ── PWM 상수 ──────────────────────────────────────────────
PWM_STEER_LEFT    = 1100.0   # 좌회전
PWM_STEER_CENTER  = 1500.0   # 직진 / 중립
PWM_STEER_RIGHT   = 1900.0   # 우회전

PWM_MOTOR_NEUTRAL = 1500.0   # 항상 정지


class ObstacleAvoidanceNode(Node):
    """
    LiDAR LaserScan을 구독해 좌/우 장애물을 감지하고
    ActuatorCommand(steering_pwm)로 회피 명령을 발행하는 노드.
    motor_pwm은 항상 1500.

    감지 구역:
        - 오른쪽: angle < 0  (ROS ENU 기준, CW 방향)
        - 왼쪽  : angle > 0  (ROS ENU 기준, CCW 방향)
        - 전방 cone (±front_angle_deg) 안의 포인트만 사용

    우선순위:
        양쪽 모두 장애물  → steer=CENTER
        오른쪽만 장애물   → steer=1100 (좌회전)
        왼쪽만 장애물     → steer=1900 (우회전)
        장애물 없음       → steer=CENTER
    """

    def __init__(self):
        super().__init__('obstacle_avoidance_node')

        # ── 파라미터 선언 ───────────────────────────────────
        self.declare_parameters(
            namespace='',
            parameters=[
                ('detection.obstacle_distance_m', 0.5),
                ('detection.front_angle_deg', 45.0),
                ('detection.ignore_radius_m', 0.3),
                ('timer_period_sec', 0.1),
            ]
        )

        # 파라미터 초기값 읽기
        self.obs_dist      = self.get_parameter('detection.obstacle_distance_m').value
        self.front_angle   = radians(self.get_parameter('detection.front_angle_deg').value)
        self.ignore_radius = self.get_parameter('detection.ignore_radius_m').value
        timer_period       = self.get_parameter('timer_period_sec').value

        # ── QoS ────────────────────────────────────────────
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

        # ── 상태 변수 ───────────────────────────────────────
        self.obstacle_left    = False
        self.obstacle_right   = False
        self.left_points_enu  = np.empty((0, 2))
        self.right_points_enu = np.empty((0, 2))
        self.last_scan_header = None

        # ── Subscriber ─────────────────────────────────────
        self.create_subscription(
            LaserScan,
            '/lidar/scan',
            self.scan_callback,
            sensor_qos
        )

        # ── Publisher ──────────────────────────────────────
        self.actuator_pub = self.create_publisher(
            ActuatorCommand,
            '/fmu/in/actuator_command',
            px4_qos
        )
        self.marker_pub = self.create_publisher(
            MarkerArray,
            '/vfh_markers',
            10
        )

        # ── 타이머 ─────────────────────────────────────────
        self.create_timer(timer_period, self.publish_command)

        # ── 실시간 파라미터 변경 콜백 등록 ─────────────────
        self.add_on_set_parameters_callback(self.parameter_callback)

        self.get_logger().info(
            f'ObstacleAvoidanceNode 시작 | '
            f'감지 거리: {self.obs_dist}m | '
            f'전방 반각: {self.get_parameter("detection.front_angle_deg").value}°'
        )

    # =================================================================
    #                   실시간 파라미터 변경 콜백
    # =================================================================
    def parameter_callback(self, params):
        """ros2 param set 호출 시 실시간으로 파라미터를 반영."""
        for param in params:
            if param.name == 'detection.obstacle_distance_m':
                self.obs_dist = param.value
                self.get_logger().info(f'[파라미터 변경] 감지 거리 → {self.obs_dist}m')

            elif param.name == 'detection.front_angle_deg':
                self.front_angle = radians(param.value)
                self.get_logger().info(f'[파라미터 변경] 전방 반각 → {param.value}°')

            elif param.name == 'detection.ignore_radius_m':
                self.ignore_radius = param.value
                self.get_logger().info(f'[파라미터 변경] 무시 반경 → {self.ignore_radius}m')

        return SetParametersResult(successful=True)

    # =================================================================
    #                        LiDAR 콜백
    # =================================================================
    def scan_callback(self, msg: LaserScan):
        """LaserScan 수신 → 좌/우 장애물 판단 및 포인트 저장."""
        self.last_scan_header = msg.header

        ranges = np.array(msg.ranges, dtype=np.float32)
        angles = np.linspace(msg.angle_min, msg.angle_max, len(ranges))

        # 1. 유효 거리 필터
        valid = (
            (ranges > self.ignore_radius) &
            (ranges < self.obs_dist) &
            np.isfinite(ranges)
        )

        # 2. 전방 cone 필터
        front = np.abs(angles) <= self.front_angle
        mask  = valid & front

        # 3. 좌/우 분리
        left_mask  = mask & (angles >= 0)
        right_mask = mask & (angles <  0)

        self.obstacle_left  = bool(np.any(left_mask))
        self.obstacle_right = bool(np.any(right_mask))

        # 4. XY 포인트 계산 (시각화용, ENU: x=전방, y=왼쪽)
        def to_xy(m):
            if not np.any(m):
                return np.empty((0, 2))
            r = ranges[m]
            a = angles[m]
            return np.column_stack((r * np.cos(a), r * np.sin(a)))

        self.left_points_enu  = to_xy(left_mask)
        self.right_points_enu = to_xy(right_mask)

    # =================================================================
    #                        명령 발행
    # =================================================================
    def publish_command(self):
        """감지 결과에 따라 steering_pwm을 결정하고 발행. motor_pwm은 항상 1500."""

        if self.obstacle_left and self.obstacle_right:
            steering_pwm = PWM_STEER_CENTER
            state = '양쪽 장애물 → 정지'
        elif self.obstacle_right:
            steering_pwm = PWM_STEER_LEFT
            state = '오른쪽 장애물 → 좌회전'
        elif self.obstacle_left:
            steering_pwm = PWM_STEER_RIGHT
            state = '왼쪽 장애물 → 우회전'
        else:
            steering_pwm = PWM_STEER_CENTER
            state = '장애물 없음 → 직진'

        # ActuatorCommand 발행
        cmd = ActuatorCommand()
        cmd.timestamp    = self.get_clock().now().nanoseconds // 1000
        cmd.motor_pwm    = PWM_MOTOR_NEUTRAL   # 항상 1500
        cmd.steering_pwm = steering_pwm
        self.actuator_pub.publish(cmd)

        self.get_logger().info(
            f'[{state}] motor={PWM_MOTOR_NEUTRAL:.0f} | steering={steering_pwm:.0f}',
            throttle_duration_sec=0.5
        )

        # MarkerArray 발행
        self._publish_markers(state, steering_pwm)

    # =================================================================
    #                        시각화
    # =================================================================
    def _publish_markers(self, state: str, steering_pwm: float):
        """장애물 포인트와 감지 구역을 /vfh_markers로 발행."""
        if self.last_scan_header is None:
            return

        header = self.last_scan_header
        ma = MarkerArray()

        # 0. 이전 마커 전체 삭제
        del_m = Marker()
        del_m.header = header
        del_m.action = Marker.DELETEALL
        ma.markers.append(del_m)

        # 1. 오른쪽 장애물 포인트 — 노란색
        ma.markers.append(self._make_points_marker(
            header, self.right_points_enu,
            ns='right_obstacles', mid=1,
            r=1.0, g=1.0, b=0.0
        ))

        # 2. 왼쪽 장애물 포인트 — 주황색
        ma.markers.append(self._make_points_marker(
            header, self.left_points_enu,
            ns='left_obstacles', mid=2,
            r=1.0, g=0.5, b=0.0
        ))

        # 3. 오른쪽 감지 구역 부채꼴
        #    장애물 감지 시 밝은 빨간색, 미감지 시 어두운 빨간색
        ma.markers.append(self._make_zone_marker(
            header, ns='zone_right', mid=3,
            angle_start=-self.front_angle, angle_end=0.0,
            radius=self.obs_dist,
            r=1.0, g=0.0, b=0.0,
            alpha=0.6 if self.obstacle_right else 0.15
        ))

        # 4. 왼쪽 감지 구역 부채꼴
        #    장애물 감지 시 밝은 파란색, 미감지 시 어두운 파란색
        ma.markers.append(self._make_zone_marker(
            header, ns='zone_left', mid=4,
            angle_start=0.0, angle_end=self.front_angle,
            radius=self.obs_dist,
            r=0.0, g=0.0, b=1.0,
            alpha=0.6 if self.obstacle_left else 0.15
        ))

        # 5. 현재 상태 텍스트
        text_m = Marker()
        text_m.header = header
        text_m.ns = 'state_text'
        text_m.id = 5
        text_m.type = Marker.TEXT_VIEW_FACING
        text_m.action = Marker.ADD
        text_m.pose.position.x = 0.0
        text_m.pose.position.y = 0.0
        text_m.pose.position.z = 1.5
        text_m.scale.z = 0.4
        text_m.color.r = 1.0
        text_m.color.g = 1.0
        text_m.color.b = 1.0
        text_m.color.a = 1.0
        text_m.text = (
            f'{state}\n'
            f'motor=1500 | steering={steering_pwm:.0f}\n'
            f'dist={self.obs_dist}m | angle=±{round(self.front_angle * 180 / 3.14159)}°'
        )
        ma.markers.append(text_m)

        self.marker_pub.publish(ma)

    def _make_points_marker(self, header, points: np.ndarray,
                             ns: str, mid: int,
                             r: float, g: float, b: float) -> Marker:
        """2D 포인트 배열을 POINTS 마커로 변환."""
        m = Marker()
        m.header = header
        m.ns = ns
        m.id = mid
        m.type = Marker.POINTS
        m.action = Marker.ADD
        m.scale.x = 0.1
        m.scale.y = 0.1
        m.color.r = r
        m.color.g = g
        m.color.b = b
        m.color.a = 0.9

        for pt in points:
            p = Point()
            p.x = float(pt[0])
            p.y = float(pt[1])
            p.z = 0.0
            m.points.append(p)

        return m

    def _make_zone_marker(self, header, ns: str, mid: int,
                           angle_start: float, angle_end: float,
                           radius: float,
                           r: float, g: float, b: float,
                           alpha: float) -> Marker:
        """감지 구역을 LINE_STRIP 마커(부채꼴)로 표현."""
        m = Marker()
        m.header = header
        m.ns = ns
        m.id = mid
        m.type = Marker.LINE_STRIP
        m.action = Marker.ADD
        m.scale.x = 0.04
        m.color.r = r
        m.color.g = g
        m.color.b = b
        m.color.a = alpha

        origin = Point(x=0.0, y=0.0, z=0.0)
        m.points.append(origin)

        n_steps = 30
        for i in range(n_steps + 1):
            a = angle_start + (angle_end - angle_start) * i / n_steps
            p = Point()
            p.x = radius * cos(a)
            p.y = radius * sin(a)
            p.z = 0.0
            m.points.append(p)

        m.points.append(origin)
        return m


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt → 종료')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()