"""Guidance utilities for the arc-based path planner."""

from dataclasses import dataclass
from math import atan2, ceil, cos, pi, sin

import numpy as np

from auto_usv_pkg.utils.math_utils import pi2pi


@dataclass(frozen=True)
class GoalGeometry:
    """Goal vector information expressed for ENU local planning."""

    distance_m: float
    rel_yaw_enu_rad: float


@dataclass(frozen=True)
class ArcEvaluation:
    """Evaluation result for one candidate arc."""

    yaw_rate_enu_rad_s: float
    trajectory_enu: np.ndarray
    collision: bool
    score: float


def compute_goal_geometry(
    curr_pos_ned,
    curr_yaw_ned,
    goal_pos_ned,
    min_goal_distance_m=0.1,
):
    """
    Compute relative goal yaw for the ENU planner from NED state/goal inputs.

    NED heading is clockwise-positive. ROS ENU yaw is counterclockwise-positive.
    Therefore, relative yaw is sign-flipped when passed to the local planner.
    """
    curr_pos_ned = np.asarray(curr_pos_ned, dtype=float)
    goal_pos_ned = np.asarray(goal_pos_ned, dtype=float)

    diff_ned = goal_pos_ned - curr_pos_ned
    distance_m = float(np.linalg.norm(diff_ned))

    if distance_m < min_goal_distance_m:
        return GoalGeometry(distance_m=distance_m, rel_yaw_enu_rad=0.0)

    goal_yaw_global_ned = atan2(diff_ned[1], diff_ned[0])
    goal_yaw_rel_ned = pi2pi(goal_yaw_global_ned - curr_yaw_ned)
    goal_yaw_rel_enu = -goal_yaw_rel_ned

    return GoalGeometry(
        distance_m=distance_m,
        rel_yaw_enu_rad=float(goal_yaw_rel_enu),
    )



def build_goal_direct_path_enu(
    distance_to_goal_m,
    rel_yaw_enu_rad,
    max_path_length_m,
    path_resolution_m=0.2,
):
    """
    Build the nominal goal-directed path in the local ENU frame.

    This path represents the route implied by compute_goal_geometry():
    move from the current body frame origin toward the goal bearing
    rel_yaw_enu_rad. It is used to decide whether collision avoidance is
    required before evaluating arc candidates.
    """
    if path_resolution_m <= 0.0:
        raise ValueError('path_resolution_m must be positive.')

    path_length_m = min(float(distance_to_goal_m), float(max_path_length_m))
    if path_length_m <= 0.0:
        return np.zeros((0, 2), dtype=float)

    point_count = max(2, int(ceil(path_length_m / path_resolution_m)) + 1)
    distances = np.linspace(0.0, path_length_m, point_count)

    direction = np.array(
        [cos(rel_yaw_enu_rad), sin(rel_yaw_enu_rad)],
        dtype=float,
    )
    return distances[:, None] * direction


def simulate_arc_enu(speed_m_s, yaw_rate_enu_rad_s, sim_time_sec, dt_sec):
    """
    Simulate a constant-speed, constant-yaw-rate trajectory in the local ENU frame.

    Local frame convention:
    - x: front
    - y: left
    - +yaw: left turn / CCW
    """
    if dt_sec <= 0.0:
        raise ValueError('dt_sec must be positive.')
    if sim_time_sec <= 0.0:
        return np.zeros((0, 2), dtype=float)

    num_steps = int(sim_time_sec / dt_sec)
    trajectory = np.zeros((num_steps, 2), dtype=float)

    x, y, theta = 0.0, 0.0, 0.0
    for step in range(num_steps):
        x += speed_m_s * cos(theta) * dt_sec
        y += speed_m_s * sin(theta) * dt_sec
        theta += yaw_rate_enu_rad_s * dt_sec
        trajectory[step] = [x, y]

    return trajectory


def score_goal_alignment(yaw_rate_enu_rad_s, goal_yaw_rel_enu_rad, sim_time_sec, weight=1.0):
    """Score how well the predicted arc end-heading aligns with the relative goal direction."""
    predicted_yaw_end_enu = yaw_rate_enu_rad_s * sim_time_sec
    angle_error = abs(pi2pi(predicted_yaw_end_enu - goal_yaw_rel_enu_rad))
    normalized_score = 1.0 - (angle_error / pi)
    return float(weight * normalized_score)


def select_best_arc(arc_evaluations):
    """Return the best non-colliding arc index, or -1 when all arcs are blocked."""
    best_idx = -1
    best_score = -float('inf')

    for idx, arc in enumerate(arc_evaluations):
        if arc.collision:
            continue
        if arc.score > best_score:
            best_score = arc.score
            best_idx = idx

    return best_idx


def compute_approach_speed(
    distance_to_goal_m,
    max_speed_m_s,
    slow_down_distance_m=5.0,
    min_speed_m_s=0.2,
):
    """Scale speed near the goal while keeping a minimum commanded forward speed."""
    if distance_to_goal_m < slow_down_distance_m:
        return float(max(min_speed_m_s, max_speed_m_s * (distance_to_goal_m / slow_down_distance_m)))
    return float(max_speed_m_s)


def yaw_rate_enu_to_absolute_yaw_ned(curr_yaw_ned, yaw_rate_enu_rad_s):
    """
    Convert an immediate ENU yaw-rate command into the absolute NED yaw command used downstream.

    The previous node published angular.z as absolute NED yaw, not as yaw rate.
    This preserves that interface.
    """
    yaw_rate_ned = -yaw_rate_enu_rad_s
    return float(pi2pi(curr_yaw_ned + yaw_rate_ned))
