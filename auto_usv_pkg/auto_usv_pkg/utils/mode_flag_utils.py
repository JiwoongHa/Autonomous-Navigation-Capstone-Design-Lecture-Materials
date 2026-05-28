"""
Mode flag checking utilities.
Provides consistent mode flag checking logic across all nodes.
"""

from px4_msgs.msg import ModeFlag


def check_mode_flag(msg: ModeFlag, flag_index: int) -> bool:
    """
    Check if a specific mode flag is active.
    
    Args:
        msg: ModeFlag message from PX4
        flag_index: Index of the mode to check (2 for VFH, 3 for Berthing)
    
    Returns:
        True if the mode is active, False otherwise
    
    Mode Logic:
        - idx 2 (VFH): modetwo > 0.5 OR modenine > 0.5
        - idx 3 (Berthing): modethree > 0.5 AND modeten > 0.5
        - idx 5 (Docking Error): modefive > 0.5
    
    NOTE: For bag file debugging, this function can be temporarily modified to always return True.
    """
    # DEBUG MODE: Uncomment the line below to bypass mode checks for bag file debugging
    # return True
    
    if flag_index == 2:
        return (msg.modetwo > 0.5) or (msg.modenine > 0.5)
    if flag_index == 3:
        return (msg.modethree > 0.5) and (msg.modeten > 0.5)
    if flag_index == 5:
        return (msg.modefive > 0.5)
    return False

