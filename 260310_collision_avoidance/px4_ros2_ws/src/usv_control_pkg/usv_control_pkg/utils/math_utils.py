"""
Mathematical utility functions.
"""

import numpy as np
import math


def normalize_angle(angle: float) -> float:
    """
    Normalize angle to [-π, π] range.
    
    Args:
        angle: Angle in radians
    
    Returns:
        Normalized angle in [-π, π] range
    """
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle


def pi2pi(rad: float) -> float:
    """
    Normalize angle to [-π, π] range using modulo operation.
    More efficient than normalize_angle for single operations.
    
    Args:
        rad: Angle in radians
    
    Returns:
        Normalized angle in [-π, π] range
    """
    return (rad + math.pi) % (2 * math.pi) - math.pi


def normalize_angle_numpy(angle: np.ndarray) -> np.ndarray:
    """
    Normalize numpy array of angles to [-π, π] range.
    
    Args:
        angle: Array of angles in radians
    
    Returns:
        Normalized angles in [-π, π] range
    """
    return (angle + np.pi) % (2 * np.pi) - np.pi

