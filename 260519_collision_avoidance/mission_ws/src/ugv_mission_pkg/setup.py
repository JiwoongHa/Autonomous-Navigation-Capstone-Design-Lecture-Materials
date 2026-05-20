from setuptools import find_packages, setup

package_name = 'ugv_mission_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/ugv_mission_launch.py']),
        ('share/' + package_name + '/config', ['config/ugv_params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='JiwoongHa',
    maintainer_email='nb1031618@gmail.com',
    description='UGV mission nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'transformer_coordinate_node = ugv_mission_pkg.transformer_coordinate_node:main',
            'collision_avoidance_node    = ugv_mission_pkg.collision_avoidance_node:main',
            'px4_mission_msg_pub_node    = ugv_mission_pkg.px4_mission_msg_pub_node:main',
        ],
    },
)