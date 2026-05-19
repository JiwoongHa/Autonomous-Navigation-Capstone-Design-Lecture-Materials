import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor 
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, ModeFlag
from std_msgs.msg import Bool, Float32
from geometry_msgs.msg import PoseStamped, Twist, Point
import numpy as np
from threading import Lock
import math

class MissionMsgPublisherforPx4(Node):
    """
    A ROS 2 node that sends Offboard control commands to PX4.
    It switches between VFH (Velocity Control) and Berthing (Position Control)
    based on PX4 ModeFlags.
    """
    
    # --- Constants ---
    # PX4 uORB Topic Names
    TOPIC_OFFBOARD_CONTROL_MODE = '/fmu/in/offboard_control_mode'
    TOPIC_TRAJECTORY_SETPOINT = '/fmu/in/trajectory_setpoint'
    TOPIC_MODE_FLAG = '/fmu/out/mode_flag'

    # Subscriber Topic Names
    TOPIC_VFH_COMMAND = '/vfh/command'             # Twist (linear.x=u_d, angular.z=yaw)
    TOPIC_BERTHING_FLAG = '/berthing_det_flag'
    TOPIC_DOCKING_INFO = '/docking_info'           # PoseStamped
    TOPIC_GOAL_NED = '/usv/state/goal_ned'         # Global Waypoint (Reference)
    TOPIC_DOCKING_ERROR = '/docking/error'         # Point (final docking error)

    def __init__(self):
        """Initializes the node, setting up publishers, subscribers, timer, and lock."""
        super().__init__('mission_msg_pub_px4')

        # --- Parameter Declaration ---
        self.declare_parameter('timer_period', 0.02)        # [sec] 50Hz
        self.declare_parameter('mode_index_vfh', 2)         # Mode ID for VFH
        self.declare_parameter('mode_index_berthing', 3)    # Mode ID for Berthing
        self.declare_parameter('mode_index_docking_error', 5)  # Mode ID for final docking error control

        # Get parameter values
        timer_period = self.get_parameter('timer_period').get_parameter_value().double_value
        self.idx_vfh = self.get_parameter('mode_index_vfh').value
        self.idx_berthing = self.get_parameter('mode_index_berthing').value
        self.idx_docking_error = self.get_parameter('mode_index_docking_error').value

        # Reliable QoS profile for control messages
        px4_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        
        # Best Effort QoS for high-rate sensors
        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # Lock for data protection
        self.data_lock = Lock()

        # Data initialization
        with self.data_lock:
            self.current_mode_flags = None
            
            # VFH State (Twist)
            self.vfh_linear_vel = 0.0 # u_d
            self.vfh_target_yaw = 0.0 # psi_d
            self.vfh_cmd_received = False
            self.vfh_cmd_stamp_ns = 0
            
            # Berthing State
            self.berthing_active_flag = False
            self.berthing_pos = [0.0, 0.0, 0.0]
            self.berthing_yaw = 0.0
            
            # Final Docking Error Command (x_be, y_be from docking_final_error_node)
            self.docking_x_be = 0.0
            self.docking_y_be = 0.0
            self.docking_cmd_received = False
            self.docking_cmd_stamp_ns = 0
            
            # Navigation Goal (Backup/Reference)
            self.nav_goal_ned = [0.0, 0.0, 0.0]

        # Create publishers
        self.offboard_control_mode_publisher = self.create_publisher(
            OffboardControlMode, self.TOPIC_OFFBOARD_CONTROL_MODE, px4_qos)
        self.trajectory_setpoint_publisher = self.create_publisher(
            TrajectorySetpoint, self.TOPIC_TRAJECTORY_SETPOINT, px4_qos)

        # Create subscribers
        self.create_subscription(ModeFlag, self.TOPIC_MODE_FLAG, self.mode_flag_callback, px4_qos)
        self.create_subscription(Twist, self.TOPIC_VFH_COMMAND, self.vfh_cmd_callback, sensor_qos)
        self.create_subscription(Bool, self.TOPIC_BERTHING_FLAG, self.berthing_flag_callback, sensor_qos)
        self.create_subscription(PoseStamped, self.TOPIC_DOCKING_INFO, self.berthing_info_callback, sensor_qos)
        self.create_subscription(Point, self.TOPIC_GOAL_NED, self.goal_ned_callback, sensor_qos)
        self.create_subscription(Point, self.TOPIC_DOCKING_ERROR, self.docking_error_callback, sensor_qos)
        
        # Timer for periodic message publishing
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info(f"PX4 Mission Pub Node initialized at {1.0/timer_period:.1f} Hz.")
        self.cmd_timeout_sec = 0.5

    # --- Subscriber Callbacks ---
    def mode_flag_callback(self, msg):
        with self.data_lock:
            self.current_mode_flags = msg

    def vfh_cmd_callback(self, msg):
        """Receives Twist message from VFH Node."""
        with self.data_lock:
            self.vfh_linear_vel = msg.linear.x  # Longitudinal velocity (u_d)
            self.vfh_target_yaw = msg.angular.z # Absolute Yaw angle (psi_d)
            self.vfh_cmd_received = True
            self.vfh_cmd_stamp_ns = self.get_clock().now().nanoseconds

    def berthing_flag_callback(self, msg):
        with self.data_lock:
            self.berthing_active_flag = msg.data

    def berthing_info_callback(self, msg):
        with self.data_lock:
            # Position
            self.berthing_pos = [msg.pose.position.x, -msg.pose.position.y, msg.pose.position.z]
            # Extract Yaw from Quaternion
            q = msg.pose.orientation
            siny_cosp = 2 * (q.w * q.z + q.x * q.y)
            cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
            self.berthing_yaw = -np.arctan2(siny_cosp, cosy_cosp)

    def goal_ned_callback(self, msg):
        with self.data_lock:
            self.nav_goal_ned = [msg.x, msg.y, msg.z]

    def docking_error_callback(self, msg: Point):
        """
        Receives final docking error from DockingGuidanceNode.
        Stores body-frame docking error (x_be, y_be). Timer callback will
        map these into velocity commands in mode 5.
        """
        with self.data_lock:
            # Store docking error as x_be, y_be (body frame)
            self.docking_x_be = msg.x
            self.docking_y_be = -msg.y
            self.docking_cmd_received = True
            self.docking_cmd_stamp_ns = self.get_clock().now().nanoseconds

    def check_mode_flag(self, msg: ModeFlag, flag_index: int) -> bool:
        if flag_index == 2:
            return (msg.modetwo > 0.5) or (msg.modenine > 0.5)
        if flag_index == 3:
            return (msg.modethree > 0.5) and (msg.modeten > 0.5)
        if flag_index == 5:
            # Simple check: use modefive > 0.5 as "Docking final error control" mode
            return msg.modefive > 0.5
        return False

    # --- Helper Functions ---
    def _check_flag(self, idx):
        if self.current_mode_flags is None: 
            return False
        return self.check_mode_flag(self.current_mode_flags, idx)

    # --- Publish Functions ---
    def publish_offboard_control_mode(self, timestamp, position=False, velocity=False, attitude=False):
        """Publishes the OffboardControlMode message."""
        msg = OffboardControlMode()
        msg.timestamp = timestamp
        msg.position = position
        msg.velocity = velocity
        msg.acceleration = False
        msg.attitude = attitude
        msg.body_rate = False
        self.offboard_control_mode_publisher.publish(msg)

    def publish_trajectory_setpoint(self, timestamp, pos=None, vel=None, yaw=0.0):
        """Publishes the TrajectorySetpoint message."""
        msg = TrajectorySetpoint()
        msg.timestamp = timestamp
        
        # Position Setpoint (NED)
        if pos is not None:
            msg.position = [float(pos[0]), float(pos[1]), float(pos[2])]
        else:
            msg.position = [0.0, 0.0, 0.0]
            
        # Velocity Setpoint (NED)
        if vel is not None:
            msg.velocity = [float(vel[0]), float(vel[1]), float(vel[2])]
        else:
            msg.velocity = [0.0, 0.0, 0.0]

        msg.yaw = float(yaw)
        self.trajectory_setpoint_publisher.publish(msg)

    # --- Main Loop ---
    def timer_callback(self):
        """Periodically called to publish control messages based on mode."""
        current_time_us = int(self.get_clock().now().nanoseconds / 1000)
        is_vfh = self._check_flag(self.idx_vfh)
        is_berthing = self._check_flag(self.idx_berthing)
        is_docking_error = self._check_flag(self.idx_docking_error)
        
        control_mode = "IDLE"

        # Logic Branching
        if is_docking_error:
            # --- DOCKING ERROR MODE (idx 5): Attitude ON, Velocity from (x_be, y_be) ---
            control_mode = "DOCKING_ERROR"
            with self.data_lock:
                x_be = self.docking_x_be
                y_be = self.docking_y_be
                cmd_age = (
                    (self.get_clock().now().nanoseconds - self.docking_cmd_stamp_ns) / 1e9
                    if self.docking_cmd_stamp_ns else None
                )
                cmd_ready = self.docking_cmd_received and cmd_age is not None and cmd_age <= self.cmd_timeout_sec

            if cmd_ready:
                # Enable velocity + attitude in OffboardControlMode
                self.publish_offboard_control_mode(
                    current_time_us,
                    position=False,
                    velocity=False,
                    attitude=True,
                )
                # Only use Y/Z components from docking error, keep X velocity zero
                self.publish_trajectory_setpoint(
                    current_time_us,
                    vel=[0.0, x_be, y_be],
                    yaw=0.0,  # Attitude control enabled; yaw reference can be extended if needed
                )
            else:
                control_mode = "DOCKING_ERROR_WAIT_CMD"

        elif is_berthing:
            # --- BERTHING MODE: Position Control ---
            control_mode = "BERTHING"
            with self.data_lock:
                target_pos = self.berthing_pos
                target_yaw = self.berthing_yaw
            # Simplified: single call with conditional position flag
            self.publish_offboard_control_mode(
                current_time_us, 
                position=self.berthing_active_flag, 
                velocity=False,
                attitude=False,
            )
            self.publish_trajectory_setpoint(current_time_us, pos=target_pos, yaw=target_yaw)

        elif is_vfh:
            # --- VFH MODE: Velocity Control (command in → immediately publish) ---
            control_mode = "VFH_VEL"
            with self.data_lock:
                u_d = self.vfh_linear_vel
                psi_d = self.vfh_target_yaw
                cmd_age = (
                    (self.get_clock().now().nanoseconds - self.vfh_cmd_stamp_ns) / 1e9
                    if self.vfh_cmd_stamp_ns else None
                )
                cmd_ready = self.vfh_cmd_received and cmd_age is not None and cmd_age <= self.cmd_timeout_sec

            if cmd_ready:
                self.publish_offboard_control_mode(
                    current_time_us,
                    position=False,
                    velocity=True,
                    attitude=False,
                )
                self.publish_trajectory_setpoint(current_time_us, vel=[u_d, 0.0, 0.0], yaw=psi_d)
            else:
                control_mode = "VFH_WAIT_CMD"
            
        else:
            # --- IDLE: Do nothing or allow Manual Control ---
            pass

        # Logging (throttled)
        if control_mode != "IDLE":
            self.get_logger().info(f"Mode: {control_mode} | Active", throttle_duration_sec=2.0)

def main(args=None):
    rclpy.init(args=args)
    node = MissionMsgPublisherforPx4()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt, shutting down.')
    except Exception as e:
        node.get_logger().error(f"Executor failed: {e}")
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
