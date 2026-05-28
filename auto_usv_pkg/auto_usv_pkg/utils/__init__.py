"""
Common utility modules for auto_usv_pkg.
"""

from .mode_flag_utils import check_mode_flag
from .math_utils import normalize_angle, pi2pi
from .pointcloud_utils import read_pointcloud_to_numpy

from .collision_avoidance import (
    DEFAULT_OBSTACLE_DISTANCE_M,
    ObstacleData,
    PlannerCommand,
    RecoveryConfig,
    RecoveryDecision,
    RecoveryState,
    check_arc_collision,
    scan_to_obstacle_data,
)

from .path_guidance import (
    ArcEvaluation,
    GoalGeometry,
    build_goal_direct_path_enu,
    compute_approach_speed,
    compute_goal_geometry,
    score_goal_alignment,
    select_best_arc,
    simulate_arc_enu,
    yaw_rate_enu_to_absolute_yaw_ned,
)

__all__ = [
    'normalize_angle',
    'pi2pi',
    'read_pointcloud_to_numpy',
    'ArcEvaluation',
    'DEFAULT_OBSTACLE_DISTANCE_M',
    'GoalGeometry',
    'ObstacleData',
    'PlannerCommand',
    'RecoveryConfig',
    'RecoveryDecision',
    'RecoveryState',
    'check_arc_collision',
    'build_goal_direct_path_enu',
    'compute_approach_speed',
    'compute_goal_geometry',
    'scan_to_obstacle_data',
    'score_goal_alignment',
    'select_best_arc',
    'simulate_arc_enu',
    'yaw_rate_enu_to_absolute_yaw_ned',
]

