from setuptools import find_packages, setup

package_name = 'ugv_collision_avoidance_lidar_example1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ansl',
    maintainer_email='ansl@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'actuator_command_publisher = ugv_collision_avoidance_lidar_example1.actuator_command_publisher:main',
        ],
    },
)
