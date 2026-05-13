import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ansl/ca_ws/install/ugv_collision_avoidance_lidar_example2'
