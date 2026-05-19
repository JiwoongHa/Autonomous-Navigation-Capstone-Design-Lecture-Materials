from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'usv_control_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='holybro',
    maintainer_email='holybro@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'coordinate_transformer_node = usv_control_pkg.coordinate_transformer_node:main',
            'lidar_pre_processor_node = usv_control_pkg.lidar_pre_processor_node:main',
            'berthing_detection_node_u_shape = usv_control_pkg.berthing_detection_node_u_shape:main',
            'simple_arc_planner_node = usv_control_pkg.simple_arc_planner_node:main',
            'px4_mission_msg_pub_node = usv_control_pkg.px4_mission_msg_pub_node:main',
        ],
    },
)
