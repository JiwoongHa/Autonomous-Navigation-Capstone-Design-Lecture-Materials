"""
ugv_mission_pkg.utils.math_utils

Common math and mode-check utilities shared across all mission nodes.
"""

from math import pi


def pi2pi(angle: float) -> float:
    """
    Wraps an angle to the range [-π, π].

    Args:
        angle: Input angle in radians.

    Returns:
        Angle wrapped to [-π, π].
    """
    return (angle + pi) % (2 * pi) - pi


def check_mode_flag(msg, flag_index: int) -> bool:
    """
    Checks PX4 ModeFlag message for a given flag index.

    Args:
        msg:        px4_msgs/ModeFlag message.
        flag_index: Integer index corresponding to a mode.

    Returns:
        True if the mode is active, False otherwise.

    Mode Index Map:
        2 → modetwo  or modenine  (VFH / Collision Avoidance)
        3 → modethree and modeten (Berthing)
        4 → modefour              (UGV Mission)
        5 → modefive              (Docking Error Control)
    """
    if flag_index == 2:
        return (msg.modetwo > 0.5) or (msg.modenine > 0.5)
    if flag_index == 3:
        return (msg.modethree > 0.5) and (msg.modeten > 0.5)
    if flag_index == 4:
        return msg.modefour > 0.5
    if flag_index == 5:
        return msg.modefive > 0.5
    return False