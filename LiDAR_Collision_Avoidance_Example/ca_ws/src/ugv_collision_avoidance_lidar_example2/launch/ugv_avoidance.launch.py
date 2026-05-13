from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    return LaunchDescription([

        # 1. Livox MID360 드라이버 + RViz
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('livox_ros_driver2'),
                    'launch_ROS2',
                    'rviz_MID360_launch.py'
                ])
            ])
        ),

        # 2. PointCloud2 → LaserScan 변환
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('pointcloud_to_laserscan'),
                    'launch',
                    'lidar_to_scan.launch.py'
                ])
            ])
        ),

        # 3. 장애물 회피 노드
        Node(
            package='ugv_collision_avoidance_lidar_example2',
            executable='obstacle_avoidance_node',
            name='obstacle_avoidance_node',
            output='screen',
            parameters=[{
                'detection.obstacle_distance_m': 0.5,
                'detection.front_angle_deg': 45.0,
                'detection.ignore_radius_m': 0.3,
                'timer_period_sec': 0.1,
            }]
        ),

    ])