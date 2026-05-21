#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from threading import Lock
import numpy as np
from pyproj import Transformer, Proj
from scipy.spatial.transform import Rotation as R

from std_msgs.msg import Float32
from px4_msgs.msg import VehicleGlobalPosition, PositionSetpointTriplet, VehicleLocalPosition, VehicleAttitude
from geometry_msgs.msg import Point


class TransformerCoordinateNode(Node):
    """
    Subscribes to global position (LLA) and local state (Heading, Velocity)
    and transforms them into the NED frame relative to a defined origin,
    publishing the results for other nodes.

    [OPT 1] Added Lock for self._cached_rotation, shared between
            attitude_callback and local_position_callback under
            MultiThreadedExecutor.
    [OPT 2] Rotation object cached in attitude_callback (where the
            quaternion actually changes) instead of being recreated on
            every local_position_callback invocation (~50 Hz).
    [OPT 3] Removed redundant _is_valid_quaternion check in
            local_position_callback since attitude_callback already
            guarantees a valid cached rotation.

    [FIX 3] wp_callback: Added msg.current.valid flag check and lon NaN
            guard to prevent invalid waypoints from being published as
            goals.

    [CLEAN 1] self.q 제거 — attitude_callback 에서 저장만 하고 어디서도
              읽히지 않는 미사용 인스턴스 변수였음.
    [CLEAN 2] self.proj_lla / self.proj_ecef 를 인스턴스 변수에서
              __init__ 지역 변수로 변경 — transformer_to_ecef 생성 후
              재사용되지 않으므로 인스턴스에 저장할 필요 없음.
    """

    def __init__(self):
        super().__init__('transformer_coordinate_node')

        px4_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        # [OPT 1] Lock for shared attitude state
        self._attitude_lock = Lock()

        # [OPT 2] Pre-cached Rotation object (identity)
        # Updated only in attitude_callback; read in local_position_callback.
        self._cached_rotation = R.from_quat([0.0, 0.0, 0.0, 1.0])  # x,y,z,w

        # --- Parameters (Origin) ---
        self.declare_parameters(
            namespace='',
            parameters=[
                ('origin.latitude',  36.395991),
                ('origin.longitude', 127.401794),
                ('origin.altitude',  25.1110),
            ])

        self.lat_origin = self.get_parameter('origin.latitude').get_parameter_value().double_value
        self.lon_origin = self.get_parameter('origin.longitude').get_parameter_value().double_value
        self.alt_origin = self.get_parameter('origin.altitude').get_parameter_value().double_value

        # --- LLA to NED Converter Initialization ---
        try:
            # [CLEAN 2] proj_lla / proj_ecef 를 지역 변수로 처리
            # transformer_to_ecef 생성에만 사용되므로 인스턴스 변수 불필요
            proj_lla  = Proj(proj='latlong', ellps='WGS84')
            proj_ecef = Proj(proj='geocent',  ellps='WGS84')
            self.transformer_to_ecef = Transformer.from_proj(proj_lla, proj_ecef)

            self.ref_x, self.ref_y, self.ref_z = self.transformer_to_ecef.transform(
                self.lon_origin, self.lat_origin, self.alt_origin
            )

            lat_rad = np.radians(self.lat_origin)
            lon_rad = np.radians(self.lon_origin)
            self.R_ecef_to_ned = np.array([
                [-np.sin(lat_rad) * np.cos(lon_rad), -np.sin(lat_rad) * np.sin(lon_rad),  np.cos(lat_rad)],
                [-np.sin(lon_rad),                    np.cos(lon_rad),                    0              ],
                [-np.cos(lat_rad) * np.cos(lon_rad), -np.cos(lat_rad) * np.sin(lon_rad), -np.sin(lat_rad)],
            ])
            self.get_logger().info(
                f"NED Origin set to LLA: ({self.lat_origin:.6f}, {self.lon_origin:.6f})"
            )

        except Exception as e:
            self.get_logger().error(f"Failed to initialize PyProj/Coordinate Transformer: {e}")
            raise

        # === Subscribers ===
        self.create_subscription(VehicleGlobalPosition,   '/fmu/out/vehicle_global_position',   self.global_position_callback, px4_qos)
        self.create_subscription(VehicleLocalPosition,    '/fmu/out/vehicle_local_position',    self.local_position_callback,  px4_qos)
        self.create_subscription(PositionSetpointTriplet, '/fmu/out/position_setpoint_triplet', self.wp_callback,              px4_qos)
        self.create_subscription(VehicleAttitude,         '/fmu/out/vehicle_attitude',          self.attitude_callback,        px4_qos)

        # === Publishers ===
        self.ned_pos_pub  = self.create_publisher(Point,   '/ugv/state/position_ned',  10)
        self.ned_goal_pub = self.create_publisher(Point,   '/ugv/state/goal_ned',      10)
        self.heading_pub  = self.create_publisher(Float32, '/ugv/state/heading',       10)
        self.velocity_pub = self.create_publisher(Point,   '/ugv/state/velocity_body', 10)

        self.get_logger().info("Coordinate Transformer Node started successfully.")

    # =================================================================
    #                       Helper Functions
    # =================================================================
    def _is_valid_quaternion(self, q: np.ndarray) -> bool:
        """Checks quaternion for correct size, finiteness, and non-zero norm."""
        return (
            q.shape == (4,)
            and np.all(np.isfinite(q))
            and np.linalg.norm(q) > 1e-6
        )

    def lla_to_ned(self, lat, lon, alt):
        """Converts LLA to NED relative to the initialized origin."""
        x, y, z = self.transformer_to_ecef.transform(lon, lat, alt)
        ecef_relative = np.array([x - self.ref_x, y - self.ref_y, z - self.ref_z])
        return self.R_ecef_to_ned @ ecef_relative

    # =================================================================
    #                        Callbacks
    # =================================================================
    def attitude_callback(self, msg: VehicleAttitude):
        """Stores incoming quaternion and updates the cached Rotation object.

        [OPT 1] Lock acquired when writing shared attitude state.
        [OPT 2] R.from_quat() called ONLY when quaternion actually changes.
        [CLEAN 1] self.q 제거 — local_position_callback 에서 사용되지
                  않으므로 인스턴스에 저장할 필요 없음.
        """
        incoming_q = np.array([msg.q[0], msg.q[1], msg.q[2], msg.q[3]])

        if not self._is_valid_quaternion(incoming_q):
            self.get_logger().warn(
                "Received invalid quaternion. Keeping previous attitude.",
                throttle_duration_sec=5.0
            )
            return

        normalized_q = incoming_q / np.linalg.norm(incoming_q)

        # SciPy expects [x, y, z, w]
        new_rotation = R.from_quat([normalized_q[1], normalized_q[2],
                                    normalized_q[3], normalized_q[0]])

        with self._attitude_lock:
            self._cached_rotation = new_rotation

    def global_position_callback(self, msg: VehicleGlobalPosition):
        """Converts incoming LLA to NED and publishes position."""
        north, east, down = self.lla_to_ned(msg.lat, msg.lon, msg.alt)
        self.ned_pos_pub.publish(Point(x=float(north), y=float(east), z=float(down)))

    def local_position_callback(self, msg: VehicleLocalPosition):
        """Publishes heading and converts NED velocity to Body-Fixed velocity.

        [OPT 1] Lock acquired when reading shared attitude state (snapshot).
        [OPT 2] Uses pre-cached Rotation object — no R.from_quat() here.
        [OPT 3] Redundant _is_valid_quaternion check removed.
        """
        self.heading_pub.publish(Float32(data=msg.heading))

        with self._attitude_lock:
            rotation_snapshot = self._cached_rotation

        ned_vel = np.array([msg.vx, msg.vy, msg.vz])

        try:
            body_vel = rotation_snapshot.apply(ned_vel, inverse=True)
            vel_msg  = Point(x=float(body_vel[0]), y=float(body_vel[1]), z=float(body_vel[2]))
        except Exception as e:
            self.get_logger().error(f"Velocity transformation (NED -> Body) failed: {e}")
            self.get_logger().warn("Publishing raw NED velocity due to error.")
            vel_msg = Point(x=float(msg.vx), y=float(msg.vy), z=float(msg.vz))

        self.velocity_pub.publish(vel_msg)

    def wp_callback(self, msg: PositionSetpointTriplet):
        """Converts current goal waypoint LLA to NED and publishes it.

        [FIX 3] Strengthened validity check:
            - msg.current.valid  : PX4 setpoint valid flag
            - np.isnan(lat/lon)  : NaN guard for both coordinates
            - lat==0 and lon==0  : zero-origin guard
        """
        if (not msg.current.valid
                or np.isnan(msg.current.lat)
                or np.isnan(msg.current.lon)
                or (msg.current.lat == 0.0 and msg.current.lon == 0.0)):
            self.get_logger().warn(
                "Invalid current waypoint received. Skipping goal.",
                throttle_duration_sec=5.0
            )
            return

        north, east, down = self.lla_to_ned(msg.current.lat, msg.current.lon, self.alt_origin)
        self.ned_goal_pub.publish(Point(x=float(north), y=float(east), z=float(down)))


def main(args=None):
    rclpy.init(args=args)
    node = TransformerCoordinateNode()
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