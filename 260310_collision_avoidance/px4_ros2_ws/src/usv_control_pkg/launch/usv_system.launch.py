import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_name = 'usv_control_pkg'

    # 1. pointcloud_to_laserscan 패키지 안의 launch 파일 경로 가져오기
    pointcloud_pkg_dir = get_package_share_directory('pointcloud_to_laserscan')
    lidar_to_scan_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pointcloud_pkg_dir, 'launch', 'lidar_to_scan.launch.py')
        )
    )

    return LaunchDescription([
        # 2. 3D -> 2D 라이다 변환 노드 먼저 실행!
        lidar_to_scan_launch,

        # 3. 기존 USV 제어 노드들 실행
        Node(package=pkg_name, executable='coordinate_transformer_node', name='coordinate_transformer_node', output='screen'),
        Node(package=pkg_name, executable='lidar_pre_processor_node', name='lidar_pre_processor_node', output='screen'),
        Node(package=pkg_name, executable='berthing_detection_node_u_shape', name='berthing_detection_node_u_shape', output='screen'),
        Node(package=pkg_name, executable='simple_arc_planner_node', name='simple_arc_planner_node', output='screen'),
        Node(package=pkg_name, executable='px4_mission_msg_pub_node', name='px4_mission_msg_pub_node', output='screen'),
    ])