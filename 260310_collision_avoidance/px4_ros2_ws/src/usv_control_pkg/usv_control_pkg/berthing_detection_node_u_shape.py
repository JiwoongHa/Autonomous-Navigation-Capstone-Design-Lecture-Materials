#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from collections import deque
import numpy as np
import cv2
from cv_bridge import CvBridge
import tf_transformations
import time
import math

from std_msgs.msg import Bool, Header
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped, Point
from px4_msgs.msg import ModeFlag
from visualization_msgs.msg import MarkerArray, Marker
from builtin_interfaces.msg import Duration

from usv_control_pkg.utils import check_mode_flag

class BerthingDetectionNode(Node):
    """
    Detects U-shaped (preferred) or L-shaped (fallback) berthing targets with Selectable Orientation.
    
    Target: The center (midpoint) of the 'Back Wall'.
    
    Features:
    - Selectable Orientation: Can search for Horizontal ('horizontal') or Vertical ('vertical') back walls.
    - Dynamic Ratio Check: Prevents noise detection by comparing back wall length to the longest side wall.
    
    Logic:
    1. Find Horizontal and Vertical lines using Hough Transform.
    2. Assign Back Wall and Side Wall candidates based on target.orientation:
       - 'horizontal': Back Wall = H-lines, Side Wall = V-lines
       - 'vertical': Back Wall = V-lines, Side Wall = H-lines
    3. Check connections:
       - U-Shape: Back wall connected to 2 Side walls (both ends).
       - L-Shape: Back wall connected to 1 Side wall (one end).
    4. Select the best shape and target the center of the Back wall.
    
    Priority: U-Shape > L-Shape > None
    """
    def __init__(self):
        super().__init__('berthing_detection_node_u_shape')

        # --- QoS Profiles ---
        px4_qos = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, durability=DurabilityPolicy.TRANSIENT_LOCAL, history=HistoryPolicy.KEEP_LAST, depth=1)
        best_effort_qos = QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, durability=DurabilityPolicy.VOLATILE, history=HistoryPolicy.KEEP_LAST, depth=10)
        
        try:
            self.bridge = CvBridge()
        except ImportError:
            self.get_logger().error("cv_bridge not installed. Cannot subscribe to BEV image.")
            self.bridge = None

        # --- Parameters ---
        self.declare_parameters(
            namespace='',
            parameters=[
                ('mode.enabled_flag', 3), 
                ('mode.stabilization_duration_sec', 1.5),
                
                # [NEW] Target Orientation Parameter
                ('target.orientation', 'horizontal'),  # 'horizontal' (Back is -) or 'vertical' (Back is |)
                
                # --- BEV Parameters ---
                ('bev.resolution_m_per_pixel', 0.01),
                ('bev.roi_x_min', -5.0), 
                ('bev.roi_y_min', 1.5), 
                
                # --- Hough Transform Parameters ---
                ('hough.canny_threshold1', 50),
                ('hough.canny_threshold2', 150),
                ('hough.threshold', 20),
                ('hough.min_line_length_m', 0.5),  # 벽면 최소 길이
                ('hough.max_line_gap_m', 0.2),    # 끊진 선 연결 허용 거리
                ('hough.angle_tolerance_deg', 20.0),
                
                # --- Structure Detection Parameters ---
                ('structure.max_corner_gap_m', 0.8),  # 뒷벽과 옆벽이 떨어져 있어도 연결로 간주할 거리
                ('structure.min_back_wall_ratio', 0.3),  # 가장 긴 선 대비 뒷벽 길이의 최소 비율 (L-Shape 노이즈 방지)
                
                # --- Stabilization/Gating Parameters ---
                ('gating.position_threshold_m', 2.0),
                ('gating.max_rejections_before_reset', 5),
            ])
        
        # Get Parameters
        self.berthing_flag_index = self.get_parameter('mode.enabled_flag').value
        self.final_stabilization_duration_sec = self.get_parameter('mode.stabilization_duration_sec').value * 4.0

        # Orientation Config
        self.target_orientation = self.get_parameter('target.orientation').value.lower()
        if self.target_orientation not in ['horizontal', 'vertical']:
            self.get_logger().warn(f"Invalid orientation '{self.target_orientation}'. Defaulting to 'horizontal'.")
            self.target_orientation = 'horizontal'
        self.get_logger().info(f"Target Orientation set to: {self.target_orientation.upper()} (Back Wall)")

        # BEV params
        self.res = self.get_parameter('bev.resolution_m_per_pixel').value
        self.x_min = self.get_parameter('bev.roi_x_min').value
        self.y_min = self.get_parameter('bev.roi_y_min').value

        # Hough params
        self.c1 = self.get_parameter('hough.canny_threshold1').value
        self.c2 = self.get_parameter('hough.canny_threshold2').value
        self.h_thresh_px = self.get_parameter('hough.threshold').value
        self.h_len_m = self.get_parameter('hough.min_line_length_m').value
        self.h_gap_m = self.get_parameter('hough.max_line_gap_m').value
        self.angle_tolerance_deg = self.get_parameter('hough.angle_tolerance_deg').value
        
        # Structure params
        self.corner_gap_px = int(self.get_parameter('structure.max_corner_gap_m').value / self.res)
        self.min_back_wall_ratio = self.get_parameter('structure.min_back_wall_ratio').value

        # Gating Params
        self.pos_thresh = self.get_parameter('gating.position_threshold_m').value
        self.max_rejections_before_reset = self.get_parameter('gating.max_rejections_before_reset').value
        
        # --- Stabilization buffers ---
        self.position_buffer = deque(maxlen=1)  # No averaging, strict update
        self.heading_buffer = deque(maxlen=1)

        # --- Gating State ---
        self.gating_rejection_counter = 0

        # --- Mode Control State ---
        self.mode_f = False
        self.mode_stable_start_time = None

        # === Subscribers ===
        self.create_subscription(Image, '/lidar/bev_image', self.bev_callback, best_effort_qos)
        self.create_subscription(ModeFlag, '/fmu/out/mode_flag', self.mode_callback, px4_qos)
        
        # === Publishers ===
        self.docking_info_publisher = self.create_publisher(PoseStamped, '/docking_info', 10)
        self.target_detected_publisher = self.create_publisher(Bool, '/berthing_det_flag', 10)
        self.debug_image_publisher = self.create_publisher(Image, '/berthing/debug_image', 10)
        self.debug_marker_pub = self.create_publisher(MarkerArray, '/berthing/debug_markers', 10)

        self.get_logger().info("Berthing Detection Node (U/L-Shape with Selectable Orientation) started.")
    
    # =================================================================
    #                       Mode Control Logic
    # =================================================================
    def _check_mode_flag(self, msg, flag_index):
        """Use common utility function."""
        return check_mode_flag(msg, flag_index)

    def mode_callback(self, msg):
        """Controls self.mode_f flag based on stabilization."""
        current_time_sec = self.get_clock().now().nanoseconds / 1e9
        raw_condition_met = self._check_mode_flag(msg, self.berthing_flag_index)

        if raw_condition_met:            
            if self.mode_stable_start_time is None:
                self.mode_stable_start_time = current_time_sec
            else:
                elapsed_sec = current_time_sec - self.mode_stable_start_time
        
                if elapsed_sec >= self.final_stabilization_duration_sec:
                    if not self.mode_f:
                        self.get_logger().info(f"Berthing Mode stabilized. Processing ENABLED.")
                    self.mode_f = True 
                
        else:
            if self.mode_f:
                self.get_logger().info("Berthing Mode condition FALSE. Processing DISABLED.")
                self.publish_berth_target_flag(False)
                
            self.mode_f = False
            self.mode_stable_start_time = None
    
    def publish_berth_target_flag(self, flag):
        """Publishes the detection flag and clears buffers if target is lost."""
        msg = Bool()
        msg.data = flag
        self.target_detected_publisher.publish(msg)
        if not flag:
            self.position_buffer.clear()
            self.heading_buffer.clear()

    # =================================================================
    #                       Core Detection Logic
    # =================================================================
    def find_u_or_l_target(self, bev_image):
        """
        Detects U or L shape based on 'target.orientation'.
        
        If target.orientation is 'horizontal': Back Wall = H-lines, Side Wall = V-lines.
        If target.orientation is 'vertical': Back Wall = V-lines, Side Wall = H-lines.
        
        Returns: (center_pixel, angle_deg, shape_type_str, debug_lines)
        """
        h_len_px = int(self.h_len_m / self.res)
        h_gap_px = int(self.h_gap_m / self.res)

        # 1. Preprocess & Hough Transform
        kernel = np.ones((5, 5), np.uint8)
        processed_bev = cv2.dilate(bev_image, kernel, iterations=1)
        edges = cv2.Canny(processed_bev, self.c1, self.c2, apertureSize=3)
        lines_p = cv2.HoughLinesP(edges, 1, np.pi / 180, self.h_thresh_px, 
                                minLineLength=h_len_px, maxLineGap=h_gap_px)
        
        if lines_p is None:
            return None, None, "None", []

        # 2. Line Classification & Global Check
        global_max_len = 0.0
        global_longest_orientation = 'None'  # 'H' or 'V'
        h_lines = []
        v_lines = []
        
        for line in lines_p:
            x1, y1, x2, y2 = line[0]
            angle_rad = np.arctan2(y2 - y1, x2 - x1)
            angle_deg = np.degrees(angle_rad)
            length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
            # Global Stat Update
            if length > global_max_len:
                global_max_len = length
                if abs(abs(angle_deg) - 90.0) < self.angle_tolerance_deg:
                    global_longest_orientation = 'V'
                elif abs(abs(angle_deg)) < self.angle_tolerance_deg or abs(abs(angle_deg) - 180.0) < self.angle_tolerance_deg:
                    global_longest_orientation = 'H'
            
            line_data = {
                'coords': (x1, y1, x2, y2), 
                'angle': angle_deg, 
                'length': length,
                'endpoints': [np.array([x1, y1]), np.array([x2, y2])]
            }
            
            # Classify as Horizontal or Vertical
            if abs(abs(angle_deg)) < self.angle_tolerance_deg or abs(abs(angle_deg) - 180.0) < self.angle_tolerance_deg:
                h_lines.append(line_data)
            elif abs(abs(angle_deg) - 90.0) < self.angle_tolerance_deg:
                v_lines.append(line_data)
            
        # 3. Assign Candidates based on Target Orientation
        back_wall_candidates = []
        side_wall_candidates = []
        
        # Danger Orientation: The orientation of the side walls (which might be confused for back walls if too long)
        danger_orientation = 'None'
        if self.target_orientation == 'horizontal':
            back_wall_candidates = h_lines
            side_wall_candidates = v_lines
            danger_orientation = 'V'  # If looking for H back wall, V side walls are the concern
        else:  # 'vertical'
            back_wall_candidates = v_lines
            side_wall_candidates = h_lines
            danger_orientation = 'H'  # If looking for V back wall, H side walls are the concern
        
        if not back_wall_candidates:
            return None, None, "None", []

        # 4. Structure Finding
        best_target = None
        best_score = -1.0
        debug_structure = []
        
        for back_line in back_wall_candidates:
            bx1, by1, bx2, by2 = back_line['coords']
            b_pts = back_line['endpoints']
            b_len = back_line['length']
            
            # --- Ratio Check ---
            # If the longest line in the scene matches the "Side Wall" orientation,
            # we must ensure our candidate "Back Wall" isn't just noise relative to that long side wall.
            if global_longest_orientation == danger_orientation and global_max_len > 0:
                ratio = b_len / global_max_len
                if ratio < self.min_back_wall_ratio:
                    continue  # Reject noise
            
            has_side1 = False
            has_side2 = False
            connected_side_lines = []
            
            # Check connections with all side wall lines
            for side_line in side_wall_candidates:
                sx1, sy1, sx2, sy2 = side_line['coords']
                s_pts = side_line['endpoints']
                
                # Find minimum distance between back wall endpoints and side wall endpoints
                min_dist = float('inf')
                for bp in b_pts:
                    for sp in s_pts:
                        dist = np.linalg.norm(bp - sp)
                        if dist < min_dist:
                            min_dist = dist
                
                if min_dist < self.corner_gap_px:
                    connected_side_lines.append(side_line['coords'])
                    # Determine connectivity to endpoints (Endpoint 1 or Endpoint 2)
                    dist_to_p1 = np.min([np.linalg.norm(sp - b_pts[0]) for sp in s_pts])
                    dist_to_p2 = np.min([np.linalg.norm(sp - b_pts[1]) for sp in s_pts])
                    
                    if dist_to_p1 < self.corner_gap_px:
                        has_side1 = True
                    if dist_to_p2 < self.corner_gap_px:
                        has_side2 = True

            # Scoring
            shape_type = "None"
            weight = 0.0
            
            if has_side1 and has_side2:
                shape_type = "U-Shape"
                weight = 2.0
            elif has_side1 or has_side2:
                shape_type = "L-Shape"
                weight = 1.0
            
            if weight > 0:
                current_score = weight * b_len
                
                if current_score > best_score:
                    best_score = current_score
                    
                    # Target Calculation: Center of the Back Wall
                    cx = (bx1 + bx2) / 2.0
                    cy = (by1 + by2) / 2.0
                    
                    best_target = (np.array([cx, cy]), back_line['angle'], shape_type)
                    debug_structure = [back_line['coords']] + connected_side_lines

        if best_target is None:
            return None, None, "None", []
        
        center_pixel, angle, s_type = best_target
        return center_pixel, angle, s_type, debug_structure

    def convert_pixel_to_robot_coords(self, center_pixel, angle_deg, img_shape):
        """Converts pixel coordinates -> robot coordinates (position, yaw)."""
        center_px_x, center_px_y = center_pixel
        img_height_px, _ = img_shape  # Use image height for Y inversion

        # Convert pixel coordinates back to robot's (livox_frame) coordinates
        robot_x = (center_px_x * self.res) + self.x_min
        # Y is inverted: (height - 1 - pixel_y)
        robot_y = ((img_height_px - 1 - center_px_y) * self.res) + self.y_min
        robot_z = 0.0 

        center_robot = np.array([robot_x, robot_y, robot_z])

        # Convert image angle to robot yaw
        # Image Y-axis maps to Robot Y-axis, Image X-axis maps to Robot X-axis.
        # Robot Yaw (0 deg) is +X (North/Forward).
        yaw_robot_rad = -np.radians(angle_deg) 

        return center_robot, yaw_robot_rad

    def publish_stable_docking_info(self, position, heading_livox_rad, timestamp):
        """Gating + Moving Average + Priming Logic."""
        accept_new_data = False
        is_primed = (len(self.position_buffer) == self.position_buffer.maxlen)

        if not self.position_buffer:
            accept_new_data = True
            self.gating_rejection_counter = 0 
        
        else:
            current_stable_pos = np.mean(self.position_buffer, axis=0)
            distance_diff = np.linalg.norm(position - current_stable_pos)
            pos_ok = distance_diff < self.pos_thresh

            if pos_ok:
                accept_new_data = True
                self.gating_rejection_counter = 0
            else:
                accept_new_data = False
                self.gating_rejection_counter += 1
                self.get_logger().warn(
                    f"Outlier rejected. Pos diff: {distance_diff:.2f}m (Thresh: {self.pos_thresh:.2f}m). "
                    f"Rejection count: {self.gating_rejection_counter}/{self.max_rejections_before_reset}",
                    throttle_duration_sec=1.0
                )

        # Anti-Stuck Filter Reset
        if is_primed and self.gating_rejection_counter >= self.max_rejections_before_reset:
            self.get_logger().warn("Gating filter possibly stuck. Clearing buffers and re-seeding.")
            self.position_buffer.clear()
            self.heading_buffer.clear()
            accept_new_data = True 
            self.gating_rejection_counter = 0 

        # Priming Outlier Reset
        if not accept_new_data and not is_primed and len(self.position_buffer) > 0:
            self.get_logger().warn("Outlier detected during priming phase. Restarting priming.")
            self.position_buffer.clear()
            self.heading_buffer.clear()
            self.gating_rejection_counter = 0
            
        # Buffer Update
        if accept_new_data:
            self.position_buffer.append(position)
            self.heading_buffer.append(heading_livox_rad) 

        # Decision to Issue
        if len(self.position_buffer) < self.position_buffer.maxlen:
            self.publish_berth_target_flag(False)
            return 
                
        # Calculate moving average and circular mean
        stable_position = np.mean(self.position_buffer, axis=0)
        sin_sum = np.sum([np.sin(h) for h in self.heading_buffer])
        cos_sum = np.sum([np.cos(h) for h in self.heading_buffer])
        stable_heading_livox = np.arctan2(sin_sum, cos_sum)
        
        # Publish PoseStamped message
        docking_info_msg = PoseStamped()
        docking_info_msg.header.stamp = timestamp
        docking_info_msg.header.frame_id = "livox_frame"
        docking_info_msg.pose.position.x = stable_position[0]
        docking_info_msg.pose.position.y = stable_position[1]
        docking_info_msg.pose.position.z = stable_position[2] 

        quat = tf_transformations.quaternion_from_euler(0, 0, stable_heading_livox)
        docking_info_msg.pose.orientation.x = quat[0]
        docking_info_msg.pose.orientation.y = quat[1]
        docking_info_msg.pose.orientation.z = quat[2]
        docking_info_msg.pose.orientation.w = quat[3]
        
        self.docking_info_publisher.publish(docking_info_msg)

        # Publish flag indicating a target is being tracked
        self.publish_berth_target_flag(True)
        
        # Publish visualization markers
        self.publish_debug_markers(stable_position, stable_heading_livox, timestamp)

    # =================================================================
    #                        Visualization
    # =================================================================
    def publish_debug_markers(self, position: np.ndarray, heading_rad: float, timestamp):
        """Publishes berthing target visualization markers."""
        header = Header()
        header.frame_id = "livox_frame"
        header.stamp = timestamp

        marray = MarkerArray()

        # Delete all previous markers
        del_marker = Marker(header=header, action=Marker.DELETEALL)
        marray.markers.append(del_marker)

        # 1. Docking position marker (sphere) - Center of Back Wall
        pos_marker = Marker(
            header=header,
            ns="berthing_pos",
            id=1,
            type=Marker.SPHERE,
            action=Marker.ADD,
            lifetime=Duration(sec=1, nanosec=0),
        )
        pos_marker.pose.position.x = float(position[0])
        pos_marker.pose.position.y = float(position[1])
        pos_marker.pose.position.z = float(position[2])
        pos_marker.scale.x = 0.5
        pos_marker.scale.y = 0.5
        pos_marker.scale.z = 0.5
        pos_marker.color.r = 0.0
        pos_marker.color.g = 1.0
        pos_marker.color.b = 1.0
        pos_marker.color.a = 0.8  # Cyan
        marray.markers.append(pos_marker)

        # 2. Heading arrow (shows docking orientation)
        arrow_marker = Marker(
            header=header,
            ns="berthing_heading",
            id=2,
            type=Marker.ARROW,
            action=Marker.ADD,
            lifetime=Duration(sec=1, nanosec=0),
        )
        arrow_marker.pose.position.x = float(position[0])
        arrow_marker.pose.position.y = float(position[1])
        arrow_marker.pose.position.z = float(position[2])
        # Set orientation from heading
        arrow_marker.pose.orientation.z = math.sin(heading_rad / 2.0)
        arrow_marker.pose.orientation.w = math.cos(heading_rad / 2.0)
        arrow_marker.scale.x = 1.5  # Arrow length
        arrow_marker.scale.y = 0.3
        arrow_marker.scale.z = 0.3
        arrow_marker.color.r = 0.0
        arrow_marker.color.g = 1.0
        arrow_marker.color.b = 0.0
        arrow_marker.color.a = 0.9
        marray.markers.append(arrow_marker)

        # 3. Text marker with position and heading info
        text_marker = Marker(
            header=header,
            ns="berthing_info",
            id=3,
            type=Marker.TEXT_VIEW_FACING,
            action=Marker.ADD,
            lifetime=Duration(sec=1, nanosec=0),
        )
        text_marker.pose.position.x = float(position[0])
        text_marker.pose.position.y = float(position[1])
        text_marker.pose.position.z = float(position[2]) + 1.0
        text_marker.scale.z = 0.5
        text_marker.color.r = 1.0
        text_marker.color.g = 1.0
        text_marker.color.b = 1.0
        text_marker.color.a = 1.0
        text_marker.text = f"Pos: ({position[0]:.2f}, {position[1]:.2f})\nHeading: {math.degrees(heading_rad):.1f}°"
        marray.markers.append(text_marker)

        try:
            self.debug_marker_pub.publish(marray)
        except Exception as e:
            self.get_logger().warn(f"Failed to publish debug markers: {e}", throttle_duration_sec=5.0)

    # =================================================================
    #                        Callback
    # =================================================================
    def bev_callback(self, msg):
        """Processes the pre-processed BEV image."""
        
        if not self.mode_f:
            return  # Processing disabled by mode control

        if self.bridge is None:
            return

        try:
            # 1. Convert ROS Image to OpenCV Image
            bev_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="mono8")
        except Exception as e:
            self.get_logger().error(f"Failed to convert BEV image: {e}")
            return
            
        # 2. Find U or L shape and get center of Back Wall
        center_pixel, angle_deg, s_type, debug_lines = self.find_u_or_l_target(bev_image)
        
        # === Debug Image Publishing ===
        if self.debug_image_publisher is not None:
            try:
                debug_img = cv2.cvtColor(bev_image, cv2.COLOR_GRAY2BGR)
                
                # Draw structure lines
                color = (0, 255, 255)  # Yellow for L-Shape
                if s_type == "U-Shape":
                    color = (0, 255, 0)  # Green for U-Shape
                
                for line_coords in debug_lines:
                    pt1 = (int(line_coords[0]), int(line_coords[1]))
                    pt2 = (int(line_coords[2]), int(line_coords[3]))
                    cv2.line(debug_img, pt1, pt2, color, 3)
                
                # Draw Target Point (Center of Back Wall)
                if center_pixel is not None:
                    cx, cy = int(center_pixel[0]), int(center_pixel[1])
                    cv2.circle(debug_img, (cx, cy), 8, (0, 0, 255), -1)  # Red Dot
                    # Show Type and configured Orientation on image
                    text = f"{s_type} ({self.target_orientation[0].upper()})"
                    cv2.putText(debug_img, text, (cx+10, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
                debug_msg = self.bridge.cv2_to_imgmsg(debug_img, "bgr8")
                debug_msg.header = msg.header
                self.debug_image_publisher.publish(debug_msg)
            except Exception as e:
                self.get_logger().warn(f"Debug image publish failed: {e}", throttle_duration_sec=5.0)
        
        # Detection failed
        if center_pixel is None:
            self.publish_berth_target_flag(False)
            return

        # 3. Convert pixel coordinates -> robot coordinates
        img_shape = bev_image.shape
        dock_info_robot = self.convert_pixel_to_robot_coords(center_pixel, angle_deg, img_shape)
        
        if dock_info_robot is None:
            self.publish_berth_target_flag(False)
            return

        # 4. Apply stabilization filter and publish
        center_robot, yaw_robot_rad = dock_info_robot
        self.publish_stable_docking_info(
            center_robot,      
            yaw_robot_rad,     
            msg.header.stamp
        )

def main(args=None):
    rclpy.init(args=args)
    
    node = BerthingDetectionNode()
    
    # Use MultiThreadedExecutor to handle high-rate BEV images and mode flag concurrently
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt received. Shutting down...')
    except Exception as e:
        node.get_logger().error(f'Unhandled exception in spin: {e}')
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()

