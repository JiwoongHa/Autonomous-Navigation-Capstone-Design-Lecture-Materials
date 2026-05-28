#!/usr/bin/env python3
"""
Dummy State Publisher Node (Indoor Debugging)

실내 디버깅을 위해 path_planner_node가 필요로 하는
세 가지 상태 토픽을 가짜 값으로 퍼블리시하는 노드.

Published Topics:
    /usv/state/position_ned  (geometry_msgs/Point)  : 현재 NED 위치 (고정: 원점)
    /usv/state/goal_ned      (geometry_msgs/Point)  : 목표 NED 위치 (파라미터로 설정)
    /usv/state/heading       (std_msgs/Float32)     : 현재 헤딩 [rad, NED]

Parameters:
    goal.north_m   : 목표 북쪽 거리 [m] (default: 5.0)
    goal.east_m    : 목표 동쪽 거리 [m] (default: 0.0)
    heading.rad    : 헤딩 [rad] (default: 0.0, 정북)
    timer_period   : 퍼블리시 주기 [sec] (default: 0.1 → 10Hz)
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from geometry_msgs.msg import Point
from std_msgs.msg import Float32


class DummyStatePubNode(Node):

    def __init__(self):
        super().__init__('dummy_state_pub_node')

        # === Parameters ===
        self.declare_parameters(
            namespace='',
            parameters=[
                ('goal.north_m', 5.0),   # 전방 5m 위치를 목표로
                ('goal.east_m',  0.0),
                ('heading.rad',  0.0),   # 정북 방향 (0.0 rad)
                ('timer_period', 0.1),   # 10Hz
            ]
        )

        self.goal_north  = self.get_parameter('goal.north_m').value
        self.goal_east   = self.get_parameter('goal.east_m').value
        self.heading_rad = self.get_parameter('heading.rad').value
        timer_period     = self.get_parameter('timer_period').value

        # === QoS ===
        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
        )

        # === Publishers ===
        self.pos_pub     = self.create_publisher(Point,   '/usv/state/position_ned', qos)
        self.goal_pub    = self.create_publisher(Point,   '/usv/state/goal_ned',     qos)
        self.heading_pub = self.create_publisher(Float32, '/usv/state/heading',      qos)

        self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info(
            f'Dummy State Publisher started. '
            f'Goal: N={self.goal_north}m, E={self.goal_east}m | '
            f'Heading: {self.heading_rad:.3f} rad'
        )

    def timer_callback(self):
        # 현재 위치: 항상 원점 (0, 0, 0)
        pos_msg = Point(x=0.0, y=0.0, z=0.0)
        self.pos_pub.publish(pos_msg)

        # 목표 위치: 파라미터로 설정된 값
        goal_msg = Point(x=self.goal_north, y=self.goal_east, z=0.0)
        self.goal_pub.publish(goal_msg)

        # 헤딩: 파라미터로 설정된 값
        heading_msg = Float32(data=self.heading_rad)
        self.heading_pub.publish(heading_msg)


def main(args=None):
    rclpy.init(args=args)
    node = DummyStatePubNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()