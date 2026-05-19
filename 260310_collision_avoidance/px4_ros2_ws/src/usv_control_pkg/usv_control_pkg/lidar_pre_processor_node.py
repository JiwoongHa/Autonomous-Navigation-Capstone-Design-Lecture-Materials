#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import numpy as np
import collections
from sensor_msgs.msg import PointCloud2, Image
from cv_bridge import CvBridge
from px4_msgs.msg import ModeFlag

from usv_control_pkg.utils import read_pointcloud_to_numpy


class LidarPreProcessorNode(Node):
    """
    원본 PointCloud2로 BEV(Bird's Eye View) 이미지 생성·발행

    - Subscribe: `/livox/lidar` (PointCloud2) for BEV 생성
    - Subscribe: `/fmu/out/mode_flag` (ModeFlag) for berthing 조건 체크
    - Publish: `/lidar/bev_image` (berthing 시각화용)
    """

    def __init__(self):
        super().__init__("lidar_pre_processor_node")

        px4_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
        )

        livox_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )

        # Parameters: BEV 설정만
        self.declare_parameters(
            namespace="",
            parameters=[
                # BEV 영역/해상도
                ("bev.resolution_m_per_pixel", 0.01),
                ("bev.roi_x_min", -5.0),
                ("bev.roi_x_max", 8.0),
                ("bev.roi_y_min", 1.5),
                ("bev.roi_y_max", 10.0),
                ("bev.accumulation_time_sec", 3.0),
            ],
        )

        # BEV 파라미터
        self.bev_res = self.get_parameter("bev.resolution_m_per_pixel").value
        self.bev_roi_x_min = self.get_parameter("bev.roi_x_min").value
        self.bev_roi_x_max = self.get_parameter("bev.roi_x_max").value
        self.bev_roi_y_min = self.get_parameter("bev.roi_y_min").value
        self.bev_roi_y_max = self.get_parameter("bev.roi_y_max").value
        self.accum_time = self.get_parameter("bev.accumulation_time_sec").value

        self.bridge = CvBridge()
        self.raw_point_buffer = collections.deque()
        self.berthing_active = False

        # Subscribers
        self.create_subscription(ModeFlag, "/fmu/out/mode_flag", self.mode_callback, px4_qos)
        self.create_subscription(PointCloud2, "/livox/lidar", self.pointcloud_callback, livox_qos)

        # Publishers
        self.bev_image_pub = self.create_publisher(Image, "/lidar/bev_image", 10)

        self.get_logger().info("LiDAR pre-processor: BEV 생성만 수행.")

    # =================================================================
    #                        Mode Callback
    # =================================================================
    def mode_callback(self, msg: ModeFlag):
        """berthing 조건: modethree > 0.5."""
        new_state = msg.modethree > 0.5
        if new_state != self.berthing_active:
            self.get_logger().info(f"Berthing BEV {'ENABLED' if new_state else 'DISABLED'}")
        self.berthing_active = new_state

    # =================================================================
    #                       Helper Functions
    # =================================================================
    def _create_bev_image(self, points_3d: np.ndarray):
        """3D 포인트를 BEV 단일 채널 이미지로 변환."""
        img_width_px = int((self.bev_roi_x_max - self.bev_roi_x_min) / self.bev_res)
        img_height_px = int((self.bev_roi_y_max - self.bev_roi_y_min) / self.bev_res)

        if img_width_px <= 0 or img_height_px <= 0:
            return None

        bev_image = np.zeros((img_height_px, img_width_px), dtype=np.uint8)

        # X -> cols, Y -> rows (좌표계를 이미지 좌표로 매핑)
        cols = ((points_3d[:, 0] - self.bev_roi_x_min) / self.bev_res).astype(int)
        rows = (img_height_px - 1 - (points_3d[:, 1] - self.bev_roi_y_min) / self.bev_res).astype(int)

        valid = (cols >= 0) & (cols < img_width_px) & (rows >= 0) & (rows < img_height_px)
        if not np.any(valid):
            return bev_image

        valid_rows = rows[valid]
        valid_cols = cols[valid]

        np.add.at(bev_image, (valid_rows, valid_cols), 255)
        bev_image = np.clip(bev_image, 0, 255).astype(np.uint8)
        return bev_image

    # =================================================================
    #                        BEV 생성 콜백
    # =================================================================
    def pointcloud_callback(self, msg: PointCloud2):
        """원본 PointCloud2를 받아 BEV 이미지를 생성해 berthing 시각화에 제공."""
        if not self.berthing_active:
            # 모드 비활성 시 버퍼 초기화로 잔상 방지
            self.raw_point_buffer.clear()
            return

        try:
            raw_points = read_pointcloud_to_numpy(msg)
        except ValueError as e:
            self.get_logger().error(f"Failed to read points from PointCloud2: {e}")
            return

        # ROI로 바로 자르고 누적(연산량 절감)
        mask_roi = (
            (raw_points[:, 0] >= self.bev_roi_x_min)
            & (raw_points[:, 0] <= self.bev_roi_x_max)
            & (raw_points[:, 1] >= self.bev_roi_y_min)
            & (raw_points[:, 1] <= self.bev_roi_y_max)
        )
        points = raw_points[mask_roi]

        if points.shape[0] == 0:
            return

        current_time = self.get_clock().now().nanoseconds / 1e9

        if points.shape[0] > 0:
            self.raw_point_buffer.append((current_time, points))

        # 슬라이딩 윈도우로 누적
        while len(self.raw_point_buffer) > 0:
            oldest_time = self.raw_point_buffer[0][0]
            if (current_time - oldest_time) > self.accum_time:
                self.raw_point_buffer.popleft()
            else:
                break

        if len(self.raw_point_buffer) == 0:
            return

        accumulated = np.vstack([p[1] for p in self.raw_point_buffer])
        bev_image = self._create_bev_image(accumulated)
        if bev_image is None:
            return

        try:
            self.bev_image_pub.publish(self.bridge.cv2_to_imgmsg(bev_image, "mono8"))
        except Exception as e:
            self.get_logger().error(f"Failed to publish BEV image: {e}")


def main(args=None):
    rclpy.init(args=args)

    node = LidarPreProcessorNode()

    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard Interrupt received. Shutting down...")
    except Exception as e:
        node.get_logger().error(f"Unhandled exception in spin: {e}")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()