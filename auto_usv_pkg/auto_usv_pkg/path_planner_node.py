#!/usr/bin/env python3
"""
Path Planner Node

Arc-based local path planner for USV guidance and collision avoidance.

Refactor notes:
- Node/file name changed from simple_arc_planner_node to path_planner_node.
- Guidance logic is delegated to auto_usv_pkg.utils.path_guidance.
- Collision avoidance and recovery logic is delegated to auto_usv_pkg.utils.collision_avoidance.
- ModeFlag/check_mode_flag/planner_enabled flow has been removed.
"""

from math import radians

import numpy as np
import rclpy
from geometry_msgs.msg import Point, Twist
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, HistoryPolicy, QoSProfile, ReliabilityPolicy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool, Float32
from visualization_msgs.msg import Marker, MarkerArray

from auto_usv_pkg.utils import (
    ArcEvaluation,
    RecoveryConfig,
    RecoveryDecision,
    RecoveryState,
    build_goal_direct_path_enu,
    check_arc_collision,
    compute_approach_speed,
    compute_goal_geometry,
    scan_to_obstacle_data,
    score_goal_alignment,
    select_best_arc,
    simulate_arc_enu,
    yaw_rate_enu_to_absolute_yaw_ned,
)


class PathPlannerNode(Node):
    """Arc-based local planner with LiDAR collision avoidance."""

    def __init__(self):
        super().__init__('path_planner_node')

        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
        )

        self._declare_parameters()
        self._load_parameters()

        # ROS ENU convention: +yaw rate is left turn / CCW.
        self.candidate_yaw_rates_enu = np.linspace(
            -self.max_yaw_rate_rad_s,
            self.max_yaw_rate_rad_s,
            self.arc_count,
        )

        # State inputs.
        self.curr_pos_ned = np.zeros(2, dtype=float)
        self.curr_yaw_ned = 0.0
        self.goal_pos_ned = np.zeros(2, dtype=float)
        self.obstacles = None
        self.last_header = None

        # Avoidance status. False means the goal-directed path is currently usable.
        self.avoidance_required = False

        # Debug / recovery state.
        self.closest_obstacle_dist = 99.9
        self.front_obstacle_dist = 99.9
        self.recovery_state = RecoveryState.NORMAL

        self.create_subscription(Point, '/usv/state/position_ned', self.pos_cb, sensor_qos)
        self.create_subscription(Float32, '/usv/state/heading', self.yaw_cb, sensor_qos)
        self.create_subscription(Point, '/usv/state/goal_ned', self.goal_cb, sensor_qos)
        self.create_subscription(LaserScan, '/lidar/scan', self.scan_cb, sensor_qos)

        self.cmd_pub = self.create_publisher(Twist, '/vfh/command', 10)
        self.avoidance_required_pub = self.create_publisher(Bool, '/vfh/oa_flag', 10)
        self.debug_pub = self.create_publisher(MarkerArray, '/vfh/debug_markers', 10)

        self.create_timer(self.period_sec, self.control_loop)
        self.get_logger().info('Path Planner Node started. ModeFlag/check_mode_flag gating is disabled.')

    def _declare_parameters(self):
        """Declare ROS parameters with defaults compatible with the previous node."""
        self.declare_parameters(
            namespace='',
            parameters=[
                ('sys.node_period_sec', 0.05),
                ('robot.max_speed_m_s', 2.3),
                ('robot.max_yaw_rate_deg_s', 75.0),
                ('robot.safety_radius_m', 0.2),
                ('plan.sim_time_sec', 3.0),
                ('plan.dt_sec', 0.2),
                ('plan.arc_count', 20),
                ('plan.goal_path_resolution_m', 0.2),
                ('lidar.ignore_radius_m', 0.6),
                ('lidar.front_angle_deg', 30.0),
                ('recovery.front_obstacle_threshold_m', 0.6),
                ('recovery.clear_distance_m', 0.6),
                ('recovery.reverse_speed_m_s', -2.3),
                ('weights.goal_align', 1.0),
                ('debug.enabled', True),
            ],
        )

    def _load_parameters(self):
        """Load ROS parameters into readable instance variables."""
        self.period_sec = float(self.get_parameter('sys.node_period_sec').value)
        self.max_speed_m_s = float(self.get_parameter('robot.max_speed_m_s').value)
        self.max_yaw_rate_rad_s = radians(float(self.get_parameter('robot.max_yaw_rate_deg_s').value))
        self.safety_radius_m = float(self.get_parameter('robot.safety_radius_m').value)

        self.sim_time_sec = float(self.get_parameter('plan.sim_time_sec').value)
        self.sim_dt_sec = float(self.get_parameter('plan.dt_sec').value)
        self.arc_count = int(self.get_parameter('plan.arc_count').value)
        self.goal_path_resolution_m = float(
            self.get_parameter('plan.goal_path_resolution_m').value
        )

        self.ignore_radius_m = float(self.get_parameter('lidar.ignore_radius_m').value)
        self.front_angle_rad = radians(float(self.get_parameter('lidar.front_angle_deg').value))

        self.recovery_config = RecoveryConfig(
            front_obstacle_threshold_m=float(
                self.get_parameter('recovery.front_obstacle_threshold_m').value
            ),
            clear_distance_m=float(self.get_parameter('recovery.clear_distance_m').value),
            reverse_speed_m_s=float(self.get_parameter('recovery.reverse_speed_m_s').value),
        )

        self.goal_align_weight = float(self.get_parameter('weights.goal_align').value)
        self.debug_enabled = bool(self.get_parameter('debug.enabled').value)

    def pos_cb(self, msg: Point):
        """Update current NED position."""
        self.curr_pos_ned = np.array([msg.x, msg.y], dtype=float)

    def yaw_cb(self, msg: Float32):
        """Update current NED heading. NED heading is clockwise-positive."""
        self.curr_yaw_ned = float(msg.data)

    def goal_cb(self, msg: Point):
        """Update goal NED position."""
        self.goal_pos_ned = np.array([msg.x, msg.y], dtype=float)

    def scan_cb(self, msg: LaserScan):
        """Convert LiDAR scan into filtered ENU obstacle points."""
        self.last_header = msg.header

        max_lookahead_m = self.max_speed_m_s * self.sim_time_sec + 2.0
        self.obstacles = scan_to_obstacle_data(
            ranges=msg.ranges,
            angle_min=msg.angle_min,
            angle_max=msg.angle_max,
            ignore_radius_m=self.ignore_radius_m,
            max_lookahead_m=max_lookahead_m,
            front_angle_rad=self.front_angle_rad,
        )

        self.closest_obstacle_dist = self.obstacles.closest_distance_m
        self.front_obstacle_dist = self.obstacles.front_distance_m

    def control_loop(self):
        """Use the direct goal path when clear; otherwise run avoidance arc planning."""
        if self.obstacles is None:
            return

        goal = compute_goal_geometry(
            curr_pos_ned=self.curr_pos_ned,
            curr_yaw_ned=self.curr_yaw_ned,
            goal_pos_ned=self.goal_pos_ned,
        )

        normal_speed = compute_approach_speed(
            distance_to_goal_m=goal.distance_m,
            max_speed_m_s=self.max_speed_m_s,
        )

        goal_direct_path_enu = self._build_goal_direct_path(goal, normal_speed)
        self.avoidance_required = check_arc_collision(
            trajectory_enu=goal_direct_path_enu,
            obstacle_points_enu=self.obstacles.points_enu,
            safety_radius_m=self.safety_radius_m,
        )

        self._publish_avoidance_required()

        # If the nominal path produced from compute_goal_geometry() is clear,
        # use it directly and skip local avoidance arc evaluation.
        if not self.avoidance_required:
            if self.recovery_state != RecoveryState.NORMAL:
                self.get_logger().info(
                    'Goal-directed path is clear. Returning to NORMAL guidance.',
                    throttle_duration_sec=1.0,
                )

            self.recovery_state = RecoveryState.NORMAL
            self._publish_command(normal_speed, goal.rel_yaw_enu_rad)

            if self.debug_enabled:
                self._publish_debug(
                    [self._make_goal_direct_evaluation(goal, goal_direct_path_enu)],
                    best_idx=0,
                    recovery_state=self.recovery_state,
                )
            return

        arc_evaluations = self._evaluate_candidate_arcs(goal.rel_yaw_enu_rad)
        best_idx = select_best_arc(arc_evaluations)

        selected_yaw_rate_enu = 0.0
        if best_idx != -1:
            selected_yaw_rate_enu = arc_evaluations[best_idx].yaw_rate_enu_rad_s

        decision = RecoveryDecision.from_planning_result(
            best_idx=best_idx,
            selected_yaw_rate_enu_rad_s=selected_yaw_rate_enu,
            normal_speed_m_s=normal_speed,
            front_obstacle_distance_m=self.front_obstacle_dist,
            current_state=self.recovery_state,
            config=self.recovery_config,
        )

        self._log_recovery_decision(decision)
        self.recovery_state = decision.next_state
        self._publish_command(decision.command.speed_m_s, decision.command.yaw_rate_enu_rad_s)

        if self.debug_enabled:
            self._publish_debug(arc_evaluations, best_idx, self.recovery_state)


    def _build_goal_direct_path(self, goal, command_speed_m_s):
        """Build the nominal path implied by compute_goal_geometry()."""
        max_path_length_m = max(
            command_speed_m_s * self.sim_time_sec,
            self.safety_radius_m,
        )
        return build_goal_direct_path_enu(
            distance_to_goal_m=goal.distance_m,
            rel_yaw_enu_rad=goal.rel_yaw_enu_rad,
            max_path_length_m=max_path_length_m,
            path_resolution_m=self.goal_path_resolution_m,
        )

    def _make_goal_direct_evaluation(self, goal, goal_direct_path_enu):
        """Represent the direct goal path in the same format as arc debug data."""
        return ArcEvaluation(
            yaw_rate_enu_rad_s=float(goal.rel_yaw_enu_rad),
            trajectory_enu=goal_direct_path_enu,
            collision=False,
            score=1.0,
        )

    def _evaluate_candidate_arcs(self, goal_yaw_rel_enu_rad):
        """Simulate, collision-check, and score every candidate yaw rate."""
        evaluations = []

        for yaw_rate_enu in self.candidate_yaw_rates_enu:
            trajectory_enu = simulate_arc_enu(
                speed_m_s=self.max_speed_m_s,
                yaw_rate_enu_rad_s=yaw_rate_enu,
                sim_time_sec=self.sim_time_sec,
                dt_sec=self.sim_dt_sec,
            )
            collision = check_arc_collision(
                trajectory_enu=trajectory_enu,
                obstacle_points_enu=self.obstacles.points_enu,
                safety_radius_m=self.safety_radius_m,
            )
            score = -float('inf')
            if not collision:
                score = score_goal_alignment(
                    yaw_rate_enu_rad_s=yaw_rate_enu,
                    goal_yaw_rel_enu_rad=goal_yaw_rel_enu_rad,
                    sim_time_sec=self.sim_time_sec,
                    weight=self.goal_align_weight,
                )

            evaluations.append(
                ArcEvaluation(
                    yaw_rate_enu_rad_s=float(yaw_rate_enu),
                    trajectory_enu=trajectory_enu,
                    collision=collision,
                    score=score,
                )
            )

        return evaluations
    
    def _publish_avoidance_required(self):
        """Publish whether the planner currently needs collision avoidance."""
        msg = Bool()
        msg.data = bool(self.avoidance_required)
        self.avoidance_required_pub.publish(msg)

    def _publish_command(self, speed_m_s, yaw_rate_enu_rad_s):
        """Publish command. angular.z is absolute NED yaw, not yaw rate."""
        yaw_absolute_ned = yaw_rate_enu_to_absolute_yaw_ned(
            curr_yaw_ned=self.curr_yaw_ned,
            yaw_rate_enu_rad_s=yaw_rate_enu_rad_s,
        )

        twist = Twist()
        twist.linear.x = float(speed_m_s)
        twist.angular.z = float(yaw_absolute_ned)
        self.cmd_pub.publish(twist)

    def _log_recovery_decision(self, decision):
        """Keep logging in the ROS node while the decision logic stays testable."""
        if not decision.log_message:
            return

        if decision.log_level == 'warn':
            self.get_logger().warn(decision.log_message)
        elif decision.log_level == 'info':
            self.get_logger().info(decision.log_message)
        elif decision.log_level == 'debug':
            self.get_logger().debug(decision.log_message)

    def _publish_debug(self, arc_evaluations, best_idx, recovery_state):
        """Publish RViz markers for candidate arcs, filtered LiDAR points, and recovery state."""
        if self.last_header is None:
            return

        marker_array = MarkerArray()
        marker_array.markers.extend(self._build_arc_markers(arc_evaluations, best_idx))
        marker_array.markers.extend(self._build_obstacle_markers())
        marker_array.markers.extend(self._build_recovery_markers(recovery_state))
        self.debug_pub.publish(marker_array)

    def _build_arc_markers(self, arc_evaluations, best_idx):
        markers = []

        for idx, arc in enumerate(arc_evaluations):
            marker = Marker()
            marker.header = self.last_header
            marker.ns = 'arcs'
            marker.id = idx
            marker.type = Marker.LINE_STRIP
            marker.action = Marker.ADD
            marker.scale.x = 0.05

            if arc.collision:
                marker.color.r = 1.0
                marker.color.a = 0.2
                marker.scale.x = 0.02
            elif idx == best_idx:
                marker.color.b = 1.0
                marker.color.a = 1.0
                marker.scale.x = 0.1
                marker.pose.position.z = 0.2
            else:
                marker.color.g = 1.0
                marker.color.a = 0.4

            for point_enu in arc.trajectory_enu:
                point = Point()
                point.x = float(point_enu[0])
                point.y = float(point_enu[1])
                marker.points.append(point)

            markers.append(marker)

        return markers

    def _build_obstacle_markers(self):
        if self.obstacles is None or len(self.obstacles.points_enu) == 0:
            return []

        marker = Marker()
        marker.header = self.last_header
        marker.ns = 'valid_points'
        marker.id = 100
        marker.type = Marker.POINTS
        marker.action = Marker.ADD
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 0.8

        for point_enu in self.obstacles.points_enu:
            point = Point()
            point.x = float(point_enu[0])
            point.y = float(point_enu[1])
            point.z = 0.0
            marker.points.append(point)

        return [marker]

    def _build_recovery_markers(self, recovery_state):
        if recovery_state == RecoveryState.NORMAL:
            return []

        marker = Marker()
        marker.header = self.last_header
        marker.ns = 'recovery_state'
        marker.id = 200
        marker.type = Marker.TEXT_VIEW_FACING
        marker.action = Marker.ADD
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 2.0
        marker.scale.z = 0.5
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        if recovery_state == RecoveryState.HOLDING:
            marker.text = f'HOLDING (Front: {self.front_obstacle_dist:.2f}m)'
        elif recovery_state == RecoveryState.REVERSING:
            marker.text = (
                f'REVERSING (Front: {self.front_obstacle_dist:.2f}m, '
                f'Speed: {self.recovery_config.reverse_speed_m_s:.2f} m/s)'
            )

        return [marker]


def main(args=None):
    """ROS entry point."""
    rclpy.init(args=args)
    node = PathPlannerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
