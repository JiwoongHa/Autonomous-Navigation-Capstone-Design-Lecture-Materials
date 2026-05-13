from setuptools import find_packages, setup

package_name = 'ugv_collision_avoidance_lidar_example2'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/ugv_avoidance.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ansl',
    maintainer_email='ansl@example.com',
    description='UGV LiDAR 기반 장애물 회피 예제 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'obstacle_avoidance_node = '
            'ugv_collision_avoidance_lidar_example2.obstacle_avoidance_node:main',
        ],
    },
)