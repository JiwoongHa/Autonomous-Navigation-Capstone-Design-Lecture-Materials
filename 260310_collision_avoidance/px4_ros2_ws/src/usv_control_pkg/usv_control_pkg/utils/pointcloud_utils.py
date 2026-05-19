"""
PointCloud2 utility functions.
"""

import numpy as np
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as point_cloud2


def read_pointcloud_to_numpy(msg: PointCloud2) -> np.ndarray:
    """
    Extract xyz points from PointCloud2 message to numpy array.
    
    Args:
        msg: PointCloud2 ROS message
    
    Returns:
        Numpy array of shape (N, 3) with x, y, z coordinates
    
    Raises:
        ValueError: If reading points fails
    """
    try:
        points_gen = point_cloud2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)
        points = np.array([[p[0], p[1], p[2]] for p in points_gen], dtype=np.float32)
        return points
    except Exception as e:
        raise ValueError(f"Failed to read points from PointCloud2: {e}")

