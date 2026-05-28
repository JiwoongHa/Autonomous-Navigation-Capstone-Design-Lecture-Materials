#!/usr/bin/env python3
"""
Launch pos_trans and path_planner_node.

Expected console_scripts in setup.py:
    pos_trans = auto_usv_pkg.coordinate_transformer_node:main
    path_planner_node = auto_usv_pkg.path_planner_node:main
"""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    
    pkg_name = 'auto_usv_pkg'
    pkg_share_dir = get_package_share_directory(pkg_name)
    param_file = os.path.join(
        pkg_share_dir,
        'config',
        'usv_params.yaml'
    )
    

    pos_trans_node = Node(
        package=pkg_name,
        executable='pos_trans',
        name='pos_trans',
        output='screen',
        emulate_tty=True,
        parameters=[param_file],
    )

    path_planner_node = Node(
        package=pkg_name,
        executable='path_planner_node',
        name='path_planner_node',
        output='screen',
        emulate_tty=True,
        parameters=[param_file],
    )

    px4_mission_node = Node(
        package=pkg_name,
        executable='px4_cmd_pub',
        name='cmd_msg_pub_px4',
        output='screen',
        emulate_tty = True,
        parameters=[param_file],
    )

    return LaunchDescription([
        # px4_mission_node,
        pos_trans_node,
        path_planner_node,
    ])
