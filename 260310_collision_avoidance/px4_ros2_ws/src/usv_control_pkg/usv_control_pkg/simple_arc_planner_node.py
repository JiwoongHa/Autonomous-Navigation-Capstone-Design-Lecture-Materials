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
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import numpy as np
from math import sin, cos, atan2, pi, radians
from std_msgs.msg import Float32
from px4_msgs.msg import ModeFlag
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Point, Twist
from visualization_msgs.msg import MarkerArray, Marker
from usv_control_pkg.utils import check_mode_flag
from usv_control_pkg.utils.math_utils import pi2pi


class SimpleArcPlannerNode(Node):
    """
    Simple arc-based path planner with collision avoidance.
    
    Generates multiple arc trajectories and selects the best one based on
    collision avoidance and goal alignment.
    """
    
    def __init__(self):
        super().__init__('simple_arc_planner_node')

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
        # Note: These default values should match usv_params.yaml
        self.declare_parameters(namespace='', parameters=[
            ## Yellow ship (USV) settings
            # ('sys.node_period_sec', 0.05),
            
            # # [Robot Kinematics]
            # ('robot.max_speed_m_s', 1.5),
            # ('robot.max_yaw_rate_deg_s', 45.0),
            # ('robot.safety_radius_m', 0.6),  # USV half-width + margin
            
            # # [Planning]
            # ('plan.sim_time_sec', 3.0),
            # ('plan.dt_sec', 0.2),
            # ('plan.arc_count', 11),  # Number of arc candidates for smooth planning
            
            # # [Recovery Behavior]
            # # front_obstacle_threshold < clear_distance (hysteresis)
            # ('recovery.front_obstacle_threshold_m', 1.0),  # ~0.67s reaction time at 1.5m/s
            # ('recovery.clear_distance_m', 1.5),  # Resume normal operation distance
            # ('recovery.reverse_speed_m_s', -0.3),  # Backward speed when all paths blocked
            
            # # [Weights]
            # ('weights.goal_align', 1.0),
            
            # ('mode.enabled_flag', 2),
            # ('debug.enabled', True)

            # UGV settings
            ('sys.node_period_sec', 0.05),
            
            # [Robot Kinematics]
            ('robot.max_speed_m_s', 2.0),
            ('robot.max_yaw_rate_deg_s', 75.0),
            ('robot.safety_radius_m', 0.20),  # USV half-width + margin
            
            # [Planning]
            ('plan.sim_time_sec', 3.0),
            ('plan.dt_sec', 0.2),
            ('plan.arc_count', 20),  # Number of arc candidates for smooth planning
            
            # [Recovery Behavior]
            # front_obstacle_threshold < clear_distance (hysteresis)
            ('recovery.front_obstacle_threshold_m', 0.6),  # ~0.67s reaction time at 1.5m/s
            ('recovery.clear_distance_m', 0.6),  # Resume normal operation distance
            ('recovery.reverse_speed_m_s',-2.4),  # Backward speed when all paths blocked
            
            # [Weights]
            ('weights.goal_align', 1.0),
            
            ('mode.enabled_flag', 2),
            ('debug.enabled', True)
        ])

        # Load Parameters
        self.period = self.get_parameter('sys.node_period_sec').value
        self.max_spd = self.get_parameter('robot.max_speed_m_s').value
        self.max_yaw_rate = radians(self.get_parameter('robot.max_yaw_rate_deg_s').value)
        self.safety_rad = self.get_parameter('robot.safety_radius_m').value
        
        self.sim_time = self.get_parameter('plan.sim_time_sec').value
        self.sim_dt = self.get_parameter('plan.dt_sec').value
        self.arc_count = self.get_parameter('plan.arc_count').value
        
        self.front_obstacle_threshold = self.get_parameter('recovery.front_obstacle_threshold_m').value
        self.clear_distance = self.get_parameter('recovery.clear_distance_m').value
        self.reverse_speed = self.get_parameter('recovery.reverse_speed_m_s').value
        
        self.w_goal = self.get_parameter('weights.goal_align').value
        
        self.enable_flag_idx = self.get_parameter('mode.enabled_flag').value
        self.debug = self.get_parameter('debug.enabled').value

        # [ENU Candidate Path Generation]
        # In ROS (ENU), positive is left turn (CCW)
        # Range: -45deg (right) ~ +45deg (left)
        self.candidate_yaw_rates = np.linspace(-self.max_yaw_rate, self.max_yaw_rate, self.arc_count)
        
        # State Variables
        self.curr_pos_ned = np.zeros(2)
        self.curr_yaw_ned = 0.0
        self.goal_pos_ned = np.zeros(2)
        self.planner_enabled = False
        self.lidar_points_enu = None
        self.last_header = None
        
        # [NEW] Debug variable for closest obstacle distance
        self.closest_obstacle_dist = 99.9
        self.front_obstacle_dist = 99.9  # Distance to closest obstacle in front direction
        
        # [NEW] Recovery behavior state
        self.recovery_state = "NORMAL"  # NORMAL, HOLDING, REVERSING

        # 🌟 [여기 두 줄 추가!]
        self.current_cmd_speed = 0.0   
        self.max_accel = 1.0

        # Publishers and Subscribers
        self.create_subscription(Point, '/usv/state/position_ned', self.pos_cb, sensor_qos)
        self.create_subscription(Float32, '/usv/state/heading', self.yaw_cb, sensor_qos)
        self.create_subscription(Point, '/usv/state/goal_ned', self.goal_cb, sensor_qos)
        self.create_subscription(LaserScan, '/lidar/scan', self.scan_cb, sensor_qos)
        self.create_subscription(ModeFlag, '/fmu/out/mode_flag', self.mode_cb, config_qos)
        
        self.cmd_pub = self.create_publisher(Twist, '/vfh/command', 10)
        self.debug_pub = self.create_publisher(MarkerArray, '/vfh/debug_markers', 10)
        
        self.create_timer(self.period, self.control_loop)
        
        self.get_logger().info("Simple Arc Planner (NED<->ENU) Started.")

    def pos_cb(self, msg):
        """Position callback."""
        self.curr_pos_ned = np.array([msg.x, msg.y])

    def yaw_cb(self, msg):
        """Heading callback - NED Heading (CW positive)."""
        self.curr_yaw_ned = msg.data

    def goal_cb(self, msg):
        """Goal position callback."""
        self.goal_pos_ned = np.array([msg.x, msg.y])

    def mode_cb(self, msg):
        """Mode flag callback."""
        self.planner_enabled = check_mode_flag(msg, self.enable_flag_idx)

    def scan_cb(self, msg):
        """Laser scan callback - processes LiDAR data in ENU frame."""
        if not self.planner_enabled:
            return

        self.last_header = msg.header
        
        # [LiDAR Processing]
        # LiDAR follows ROS standard (ENU, CCW). Use as is.
        # x = Front, y = Left
        ranges = np.array(msg.ranges)
        angles = np.linspace(msg.angle_min, msg.angle_max, len(ranges))
        
        # [핵심 수정] 자기 자신 필터링 (0.6m 이내는 무시)
        # 배의 구조물이나 앞머리가 찍히는 것을 방지
        # ignore_radius = 0.6
        ignore_radius = 0.3
        max_lookahead = self.max_spd * self.sim_time + 2.0
        
        valid = (ranges > ignore_radius) & (ranges < max_lookahead)
        ranges = ranges[valid]
        angles = angles[valid]
        
        xs = ranges * np.cos(angles)
        ys = ranges * np.sin(angles)
        self.lidar_points_enu = np.column_stack((xs, ys))
        
        # [NEW] Track closest obstacle distance for debugging
        if len(ranges) > 0:
            self.closest_obstacle_dist = np.min(ranges)
            
            # Calculate front obstacle distance (within ±30 degrees)
            front_angle_range = radians(30.0)  # ±30 degrees
            front_mask = np.abs(angles) < front_angle_range
            if np.any(front_mask):
                self.front_obstacle_dist = np.min(ranges[front_mask])
            else:
                self.front_obstacle_dist = 99.9
        else:
            self.closest_obstacle_dist = 99.9
            self.front_obstacle_dist = 99.9

    def control_loop(self):
        """Main control loop - computes and publishes velocity commands."""
        if not self.planner_enabled or self.lidar_points_enu is None:
            return

        # ==========================================================
        # 1. Goal Vector Calculation (NED -> ENU Conversion)
        # ==========================================================
        diff_ned = self.goal_pos_ned - self.curr_pos_ned
        dist_to_goal = np.linalg.norm(diff_ned)
        
        # Handle case when goal is at origin or too close
        if dist_to_goal < 0.1:
            goal_yaw_rel_enu = 0.0
        else:
            # NED Global Yaw (North=0, CW+)
            goal_yaw_global_ned = atan2(diff_ned[1], diff_ned[0])
            
            # Relative Yaw in NED (Target - Current)
            # Positive value means target is to the right (CW)
            goal_yaw_rel_ned = pi2pi(goal_yaw_global_ned - self.curr_yaw_ned)
            
            # [Core Conversion] NED (right turn+) -> ENU (left turn+)
            # Right turn 30deg (NED +30) is -30deg (ENU -30) in ROS
            goal_yaw_rel_enu = -goal_yaw_rel_ned

        # ==========================================================
        # 2. Evaluate Arcs (All calculation in ENU)
        # ==========================================================
        best_idx = -1
        best_score = -float('inf')
        debug_arcs = []
        
        for i, yaw_rate_enu in enumerate(self.candidate_yaw_rates):
            # (A) Simulation (ENU Frame: x=Front, y=Left)
            trajectory = self._simulate_arc(self.max_spd, yaw_rate_enu)
            
            # (B) Collision Check (LiDAR points are also in ENU)
            is_collision = self._check_collision(trajectory)
            
            # (C) Score Calculation
            score = -float('inf')
            if not is_collision:
                # Predicted end angle (ENU)
                predicted_yaw_end_enu = yaw_rate_enu * self.sim_time
                
                # Angle difference from goal (ENU frame)
                angle_diff = abs(pi2pi(predicted_yaw_end_enu - goal_yaw_rel_enu))
                score = 1.0 - (angle_diff / pi)
            
            debug_arcs.append({
                'traj': trajectory,
                'collision': is_collision,
                'score': score
            })
            
            if score > best_score:
                best_score = score
                best_idx = i

        # ==========================================================
        # 3. Output Command (Convert yaw rate to absolute yaw)
        # ==========================================================
        # NOTE: px4_mission_msg_pub_node expects absolute yaw (not yaw rate)
        # So we need to integrate yaw rate to get target absolute yaw
        cmd_speed = 0.0
        cmd_yaw_rate_enu = 0.0
        
        if best_idx != -1:
            # Path found: Check if we should exit recovery state
            if self.front_obstacle_dist >= self.clear_distance:
                # Front is clear: Reset recovery state and use normal planning
                if self.recovery_state != "NORMAL":
                    self.get_logger().info(
                        f"Path found and front clear ({self.front_obstacle_dist:.2f}m >= {self.clear_distance:.2f}m). "
                        f"Resuming normal operation."
                    )
                self.recovery_state = "NORMAL"
                
                if dist_to_goal < 5.0:
                    cmd_speed = max(2.0, self.max_spd * (dist_to_goal / 5.0))
                else:
                    cmd_speed = self.max_spd
                cmd_yaw_rate_enu = self.candidate_yaw_rates[best_idx]
            else:
                # Path found but front still too close: Continue holding/reversing
                if self.front_obstacle_dist < self.front_obstacle_threshold:
                    # Front obstacle too close: Hold or reverse
                    if self.recovery_state == "NORMAL":
                        self.recovery_state = "HOLDING"
                        self.get_logger().warn(
                            f"Path found but front obstacle too close ({self.front_obstacle_dist:.2f}m < {self.front_obstacle_threshold:.2f}m). "
                            f"Holding heading.",
                            throttle_duration_sec=1.0
                        )
                    elif self.recovery_state == "HOLDING":
                        self.recovery_state = "REVERSING"
                    
                    if self.recovery_state == "HOLDING":
                        cmd_speed = 0.0
                        cmd_yaw_rate_enu = 0.0
                    else:  # REVERSING
                        cmd_speed = self.reverse_speed
                        cmd_yaw_rate_enu = 0.0
                else:
                    # Front obstacle at safe distance: Normal operation
                    self.recovery_state = "NORMAL"
                    if dist_to_goal < 5.0:
                        cmd_speed = max(2.0, self.max_spd * (dist_to_goal / 5.0))
                    else:
                        cmd_speed = self.max_spd
                    cmd_yaw_rate_enu = self.candidate_yaw_rates[best_idx]
        else:
            # All Blocked: Recovery behavior based on front obstacle distance
            if self.front_obstacle_dist < self.front_obstacle_threshold:
                # Front obstacle too close: Hold or reverse
                if self.recovery_state == "NORMAL":
                    self.recovery_state = "HOLDING"
                    self.get_logger().warn(
                        f"All Paths Blocked! Front obstacle too close ({self.front_obstacle_dist:.2f}m < {self.front_obstacle_threshold:.2f}m). "
                        f"Holding heading.",
                        throttle_duration_sec=2.0
                    )
                elif self.recovery_state == "HOLDING":
                    self.recovery_state = "REVERSING"
                
                if self.recovery_state == "HOLDING":
                    # HOLDING: Maintain current heading, stop forward motion
                    cmd_speed = 0.0
                    cmd_yaw_rate_enu = 0.0  # Keep current heading
                    self.get_logger().debug(
                        f"Holding heading... Front obs: {self.front_obstacle_dist:.2f}m",
                        throttle_duration_sec=0.5
                    )
                else:  # REVERSING
                    # REVERSING: Maintain current heading, move backward
                    if self.front_obstacle_dist >= self.clear_distance:
                        # Front cleared: Stop reversing, go back to holding
                        if self.recovery_state == "REVERSING":
                            self.get_logger().info(
                                f"Front cleared ({self.front_obstacle_dist:.2f}m >= {self.clear_distance:.2f}m). "
                                f"Stopping reverse."
                            )
                        self.recovery_state = "HOLDING"
                        cmd_speed = 0.0
                        cmd_yaw_rate_enu = 0.0
                    else:
                        #Continue reversing
                        cmd_speed = self.reverse_speed  # Negative speed for backward
                        
                        # 🌟 [NEW] 개선 제안 1: 후진 시 조향각 추가 (무한 루프 탈출)
                        # 목표 지점이 왼쪽(+)에 있으면 후진할 때 차 앞머리가 왼쪽을 향하도록 우회전(-) 조향
                        # (최대 조향각의 50% 정도만 사용하여 부드럽게 곡선 후진)
                        cmd_yaw_rate_enu = -np.sign(goal_yaw_rel_enu) * (self.max_yaw_rate * 0.5)
                        
                        self.get_logger().debug(
                            f"Reversing with steering... Front obs: {self.front_obstacle_dist:.2f}m",
                            throttle_duration_sec=0.5
                        )
            else:
                # Front obstacle at safe distance but all paths blocked: Try to find path
                # This shouldn't happen often, but handle it gracefully
                self.recovery_state = "NORMAL"
                cmd_speed = 0.0
                cmd_yaw_rate_enu = 0.0
                self.get_logger().warn(
                    f"All paths blocked but front clear ({self.front_obstacle_dist:.2f}m). Waiting...",
                    throttle_duration_sec=2.0
                )

        # Convert yaw rate to absolute target yaw
        # NOTE: yaw_rate is used directly (not multiplied by sim_time) as it represents
        # the immediate desired yaw change. The integration is handled by the control period.
        # Convert ENU yaw rate to NED yaw rate first
        cmd_yaw_rate_ned = -cmd_yaw_rate_enu  # ENU to NED conversion
        
        # Calculate target absolute yaw in NED frame
        # Current yaw + yaw rate (immediate change, not integrated over sim_time)
        cmd_yaw_absolute_ned = pi2pi(self.curr_yaw_ned + cmd_yaw_rate_ned)

        # 🌟 [NEW] 전진/후진 모두 부드럽게 출발하는 스마트 가속 필터
        
        speed_step = self.max_accel * self.period  # 한 번에 변할 수 있는 최대 속도폭

        if cmd_speed == 0.0:
            # 1. 긴급 정지: 장애물을 만나면 즉시(0초 만에) 브레이크!
            self.current_cmd_speed = 0.0
            
        elif cmd_speed > 0.0 and cmd_speed > self.current_cmd_speed:
            # 2. 전진 가속: 엑셀을 부드럽게 밟음
            self.current_cmd_speed = min(cmd_speed, self.current_cmd_speed + speed_step)
            
        elif cmd_speed < 0.0 and cmd_speed < self.current_cmd_speed:
            # 3. 후진 가속: 후진 기어 넣고 엑셀을 부드럽게 밟음
            self.current_cmd_speed = max(cmd_speed, self.current_cmd_speed - speed_step)
            
        else:
            # 4. 그 외 (주행 중 감속 등): 목표 속도에 즉각 맞춤
            self.current_cmd_speed = cmd_speed
        
        twist = Twist()
        twist.linear.x = float(self.current_cmd_speed)
        twist.angular.z = float(cmd_yaw_absolute_ned)  # Absolute yaw (consistent with other nodes)
        self.cmd_pub.publish(twist)
        
        if self.debug:
            self._publish_debug(debug_arcs, best_idx, self.recovery_state)

    def _simulate_arc(self, v, w):
        """
        Simulate arc trajectory in ENU frame.
        
        Args:
            v: Linear velocity (m/s)
            w: Angular velocity (rad/s, ENU frame)
            
        Returns:
            Trajectory array (num_steps, 2) in ENU frame
        """
        num_steps = int(self.sim_time / self.sim_dt)
        traj = np.zeros((num_steps, 2))
        x, y, theta = 0.0, 0.0, 0.0
        
        for i in range(num_steps):
            x += v * cos(theta) * self.sim_dt
            y += v * sin(theta) * self.sim_dt
            theta += w * self.sim_dt
            traj[i] = [x, y]
        
        return traj

    def _check_collision(self, trajectory):
        """
        Check if trajectory collides with obstacles.
        
        Args:
            trajectory: Trajectory array (num_steps, 2) in ENU frame
            
        Returns:
            True if collision detected, False otherwise
        """
        if self.lidar_points_enu is None or len(self.lidar_points_enu) == 0:
            return False
        
        # Simple proximity check
        for pt in trajectory:
            dists_sq = (
                (self.lidar_points_enu[:, 0] - pt[0])**2 + 
                (self.lidar_points_enu[:, 1] - pt[1])**2
            )
            if np.min(dists_sq) < (self.safety_rad**2):
                return True
        
        return False

    def _publish_debug(self, debug_arcs, best_idx, recovery_state="NORMAL"):
        """
        Publish debug markers for visualization in RViz.
        
        Args:
            debug_arcs: List of arc information dictionaries
            best_idx: Index of best selected arc
            recovery_state: Current recovery state (NORMAL, HOLDING, REVERSING)
        """
        if self.last_header is None:
            return
        
        ma = MarkerArray()
        
        # RViz is ENU. So we publish trajectory as is (since calculation was ENU)
        for i, info in enumerate(debug_arcs):
            traj = info['traj']
            is_coll = info['collision']
            
            m = Marker()
            m.header = self.last_header
            m.ns = "arcs"
            m.id = i
            m.type = Marker.LINE_STRIP
            m.action = Marker.ADD
            m.scale.x = 0.05
            
            if is_coll:
                m.color.r = 1.0
                m.color.a = 0.2  # Red (Collision)
                m.scale.x = 0.02
            elif i == best_idx:
                m.color.b = 1.0
                m.color.a = 1.0  # Blue (Selected)
                m.scale.x = 0.1
                m.pose.position.z = 0.2
            else:
                m.color.g = 1.0
                m.color.a = 0.4  # Green (Safe)
            
            for pt in traj:
                p = Point()
                p.x = pt[0]
                p.y = pt[1]
                m.points.append(p)
            
            ma.markers.append(m)
        
        # [NEW] Visualize LiDAR points used for collision check
        if self.lidar_points_enu is not None and len(self.lidar_points_enu) > 0:
            m_pts = Marker()
            m_pts.header = self.last_header
            m_pts.ns = "valid_points"
            m_pts.id = 100
            m_pts.type = Marker.POINTS
            m_pts.action = Marker.ADD
            m_pts.scale.x = 0.1
            m_pts.scale.y = 0.1
            m_pts.color.r = 1.0
            m_pts.color.g = 1.0
            m_pts.color.b = 0.0
            m_pts.color.a = 0.8  # Yellow points
            
            for pt in self.lidar_points_enu:
                p = Point()
                p.x = pt[0]
                p.y = pt[1]
                p.z = 0.0
                m_pts.points.append(p)
            
            ma.markers.append(m_pts)
        
        # [NEW] Visualize recovery state as text marker
        if recovery_state != "NORMAL":
            m_text = Marker()
            m_text.header = self.last_header
            m_text.ns = "recovery_state"
            m_text.id = 200
            m_text.type = Marker.TEXT_VIEW_FACING
            m_text.action = Marker.ADD
            m_text.pose.position.x = 0.0
            m_text.pose.position.y = 0.0
            m_text.pose.position.z = 2.0
            m_text.scale.z = 0.5
            m_text.color.r = 1.0
            m_text.color.g = 0.0
            m_text.color.b = 0.0
            m_text.color.a = 1.0
            
            if recovery_state == "HOLDING":
                m_text.text = f"HOLDING (Front: {self.front_obstacle_dist:.2f}m)"
            elif recovery_state == "REVERSING":
                m_text.text = f"REVERSING (Front: {self.front_obstacle_dist:.2f}m, Speed: {self.reverse_speed:.2f} m/s)"
            
            ma.markers.append(m_text)
        
        self.debug_pub.publish(ma)


def main(args=None):
    """Main entry point."""
    rclpy.init(args=args)
    node = SimpleArcPlannerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

