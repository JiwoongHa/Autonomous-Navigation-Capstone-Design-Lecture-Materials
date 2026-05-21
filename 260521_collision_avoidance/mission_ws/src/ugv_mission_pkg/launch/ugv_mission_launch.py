from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    # --- ugv_params.yaml 경로 ---
    params_file = os.path.join(
        get_package_share_directory('ugv_mission_pkg'),
        'config', 'ugv_params.yaml'
    )

    # --- pointcloud_to_laserscan launch 포함 ---
    lidar_to_scan_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('pointcloud_to_laserscan'),
                'launch',
                'lidar_to_scan.launch.py'
            )
        )
    )

    # --- transformer_coordinate_node ---
    transformer_coordinate_node = Node(
        package='ugv_mission_pkg',
        executable='transformer_coordinate_node',
        name='transformer_coordinate_node',
        output='screen',
        parameters=[params_file],  # ← yaml에서 origin 좌표 읽어옴
    )

    # --- collision_avoidance_node ---
    collision_avoidance_node = Node(
        package='ugv_mission_pkg',
        executable='collision_avoidance_node',
        name='collision_avoidance_node',
        output='screen',
    )

    # --- px4_mission_msg_pub_node ---
    px4_mission_msg_pub_node = Node(
        package='ugv_mission_pkg',
        executable='px4_mission_msg_pub_node',
        name='px4_mission_msg_pub_node',
        output='screen',
    )

    return LaunchDescription([
        lidar_to_scan_launch,
        transformer_coordinate_node,
        collision_avoidance_node,
        px4_mission_msg_pub_node,
    ])