"""Collision-avoidance and recovery utilities for the path planner."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np


DEFAULT_OBSTACLE_DISTANCE_M = 99.9


class RecoveryState(str, Enum):
    """Planner recovery states."""

    NORMAL = 'NORMAL'
    HOLDING = 'HOLDING'
    REVERSING = 'REVERSING'


@dataclass(frozen=True)
class ObstacleData:
    """Filtered LiDAR obstacle information in the local ENU frame."""

    points_enu: np.ndarray
    closest_distance_m: float = DEFAULT_OBSTACLE_DISTANCE_M
    front_distance_m: float = DEFAULT_OBSTACLE_DISTANCE_M


@dataclass(frozen=True)
class RecoveryConfig:
    """Recovery thresholds and speeds."""

    front_obstacle_threshold_m: float
    clear_distance_m: float
    reverse_speed_m_s: float
    reverse_turn_rate_rad_s: float = 0.0


@dataclass(frozen=True)
class PlannerCommand:
    """Planner output before conversion to ROS Twist."""

    speed_m_s: float
    yaw_rate_enu_rad_s: float


@dataclass(frozen=True)
class RecoveryDecision:
    """Recovery result for one control cycle."""

    command: PlannerCommand
    next_state: RecoveryState
    log_level: Optional[str] = None
    log_message: Optional[str] = None
    throttle_sec: float = 1.0

    @classmethod
    def from_planning_result(
        cls,
        best_idx,
        selected_yaw_rate_enu_rad_s,
        normal_speed_m_s,
        front_obstacle_distance_m,
        current_state,
        config,
        obstacle_points_enu=None,
    ):
        """Choose normal, hold, or reverse command from arc-planning and obstacle results."""
        current_state = normalize_recovery_state(current_state)
        path_found = best_idx != -1

        if path_found:
            return _decision_when_path_found(
                selected_yaw_rate_enu_rad_s=selected_yaw_rate_enu_rad_s,
                normal_speed_m_s=normal_speed_m_s,
                front_obstacle_distance_m=front_obstacle_distance_m,
                current_state=current_state,
                config=config,
                obstacle_points_enu=obstacle_points_enu,
            )

        return _decision_when_all_paths_blocked(
            front_obstacle_distance_m=front_obstacle_distance_m,
            current_state=current_state,
            config=config,
            obstacle_points_enu=obstacle_points_enu,
        )


def normalize_recovery_state(state):
    """Convert strings or enum values to RecoveryState."""
    if isinstance(state, RecoveryState):
        return state
    try:
        return RecoveryState(str(state))
    except ValueError:
        return RecoveryState.NORMAL

def keep_contiguous_scan_clusters(
    ranges,
    angles,
    valid_mask,
    min_cluster_points=3,
    max_cluster_gap_m=0.35,
):
    """Keep only scan returns that belong to contiguous obstacle clusters."""
    if min_cluster_points <= 1:
        return valid_mask

    ranges = np.asarray(ranges, dtype=float)
    angles = np.asarray(angles, dtype=float)
    valid_mask = np.asarray(valid_mask, dtype=bool)

    cluster_mask = np.zeros_like(valid_mask, dtype=bool)
    valid_indices = np.where(valid_mask)[0]

    if len(valid_indices) == 0:
        return cluster_mask

    xs = ranges * np.cos(angles)
    ys = ranges * np.sin(angles)
    points = np.column_stack((xs, ys))

    def commit_cluster(cluster_indices):
        if len(cluster_indices) >= min_cluster_points:
            cluster_mask[cluster_indices] = True

    cluster = [int(valid_indices[0])]
    prev_idx = int(valid_indices[0])

    for idx in valid_indices[1:]:
        idx = int(idx)

        is_scan_contiguous = idx == prev_idx + 1
        gap_m = np.linalg.norm(points[idx] - points[prev_idx])

        if is_scan_contiguous and np.isfinite(gap_m) and gap_m <= max_cluster_gap_m:
            cluster.append(idx)
        else:
            commit_cluster(cluster)
            cluster = [idx]

        prev_idx = idx

    commit_cluster(cluster)
    return cluster_mask

def scan_to_obstacle_data(
    ranges,
    angle_min,
    angle_max,
    ignore_radius_m,
    max_lookahead_m,
    front_angle_rad,
    min_cluster_points=1,
    max_cluster_gap_m=0.35,
):
    """Filter LaserScan ranges and convert valid returns to local ENU obstacle points."""
    ranges = np.asarray(ranges, dtype=float)
    if len(ranges) == 0:
        return ObstacleData(points_enu=np.zeros((0, 2), dtype=float))

    angles = np.linspace(angle_min, angle_max, len(ranges))
    valid_mask = (
        np.isfinite(ranges)
        & (ranges > ignore_radius_m)
        & (ranges < max_lookahead_m)
    )

    if min_cluster_points > 1:
        valid_mask = keep_contiguous_scan_clusters(
            ranges=ranges,
            angles=angles,
            valid_mask=valid_mask,
            min_cluster_points=min_cluster_points,
            max_cluster_gap_m=max_cluster_gap_m,
        )

    valid_ranges = ranges[valid_mask]
    valid_angles = angles[valid_mask]

    if len(valid_ranges) == 0:
        return ObstacleData(points_enu=np.zeros((0, 2), dtype=float))

    points_enu = np.column_stack(
        (
            valid_ranges * np.cos(valid_angles),
            valid_ranges * np.sin(valid_angles),
        )
    )

    closest_distance_m = float(np.min(valid_ranges))
    front_mask = np.abs(valid_angles) < front_angle_rad
    front_distance_m = DEFAULT_OBSTACLE_DISTANCE_M
    if np.any(front_mask):
        front_distance_m = float(np.min(valid_ranges[front_mask]))

    return ObstacleData(
        points_enu=points_enu,
        closest_distance_m=closest_distance_m,
        front_distance_m=front_distance_m,
    )


def check_arc_collision(trajectory_enu, obstacle_points_enu, safety_radius_m):
    """Return True when any trajectory point is within safety radius of an obstacle point."""
    trajectory_enu = np.asarray(trajectory_enu, dtype=float)
    obstacle_points_enu = np.asarray(obstacle_points_enu, dtype=float)

    if len(trajectory_enu) == 0 or len(obstacle_points_enu) == 0:
        return False

    safety_radius_sq = safety_radius_m**2
    for trajectory_point in trajectory_enu:
        diff = obstacle_points_enu - trajectory_point
        distance_sq = np.sum(diff * diff, axis=1)
        if np.any(distance_sq < safety_radius_sq):
            return True

    return False


def compute_reverse_escape_yaw_rate_enu(
    obstacle_points_enu,
    reverse_turn_rate_rad_s,
    front_only=True,
    deadband_m=0.05,
):
    """Return a yaw command that turns away from the obstacle-heavy side while reversing.

    Local ENU convention:
    - x: front
    - y: left
    - positive yaw rate: left turn / CCW

    If obstacle points are biased to the left side (positive y), return a negative yaw rate
    so the commanded heading turns right. If obstacle points are biased to the right side
    (negative y), return a positive yaw rate so the commanded heading turns left.
    """
    turn_rate = abs(float(reverse_turn_rate_rad_s))
    if turn_rate <= 0.0:
        return 0.0

    points = np.asarray(obstacle_points_enu, dtype=float)
    if points.ndim != 2 or points.shape[1] != 2 or len(points) == 0:
        return 0.0

    finite_mask = np.isfinite(points).all(axis=1)
    points = points[finite_mask]
    if len(points) == 0:
        return 0.0

    if front_only:
        front_points = points[points[:, 0] > 0.0]
        if len(front_points) > 0:
            points = front_points

    distance_sq = np.sum(points * points, axis=1)
    weights = 1.0 / np.maximum(distance_sq, 1.0e-3)
    lateral_bias_m = float(np.sum(weights * points[:, 1]) / np.sum(weights))

    if abs(lateral_bias_m) < deadband_m:
        return 0.0

    # Obstacle left(+y) -> turn right(-yaw). Obstacle right(-y) -> turn left(+yaw).
    return -turn_rate if lateral_bias_m > 0.0 else turn_rate


def _reverse_command(config, obstacle_points_enu):
    """Build a reverse command with an escape yaw rate away from obstacles."""
    escape_yaw_rate_enu = compute_reverse_escape_yaw_rate_enu(
        obstacle_points_enu=obstacle_points_enu,
        reverse_turn_rate_rad_s=config.reverse_turn_rate_rad_s,
    )
    return PlannerCommand(config.reverse_speed_m_s, escape_yaw_rate_enu)


def _decision_when_path_found(
    selected_yaw_rate_enu_rad_s,
    normal_speed_m_s,
    front_obstacle_distance_m,
    current_state,
    config,
    obstacle_points_enu=None,
):
    """Handle recovery while a non-colliding arc exists.

    State transition policy:
    - clear front distance           -> NORMAL
    - NORMAL + close front obstacle  -> HOLDING for one control cycle
    - HOLDING + close front obstacle -> REVERSING
    - REVERSING continues until the front distance reaches clear_distance_m
    """
    if front_obstacle_distance_m >= config.clear_distance_m:
        log_message = None
        if current_state != RecoveryState.NORMAL:
            log_message = (
                f'Path found and front clear '
                f'({front_obstacle_distance_m:.2f}m >= {config.clear_distance_m:.2f}m). '
                f'Resuming normal operation.'
            )
        return RecoveryDecision(
            command=PlannerCommand(normal_speed_m_s, selected_yaw_rate_enu_rad_s),
            next_state=RecoveryState.NORMAL,
            log_level='info' if log_message else None,
            log_message=log_message,
            throttle_sec=1.0,
        )

    if current_state == RecoveryState.REVERSING:
        reverse_command = _reverse_command(config, obstacle_points_enu)
        return RecoveryDecision(
            command=reverse_command,
            next_state=RecoveryState.REVERSING,
            log_level='debug',
            log_message=(
                f'REVERSING: front obstacle {front_obstacle_distance_m:.2f}m. '
                f'Continuing reverse with escape yaw rate '
                f'{reverse_command.yaw_rate_enu_rad_s:.3f} rad/s until '
                f'{config.clear_distance_m:.2f}m clear distance.'
            ),
            throttle_sec=0.5,
        )

    if front_obstacle_distance_m < config.front_obstacle_threshold_m:
        if current_state == RecoveryState.NORMAL:
            return RecoveryDecision(
                command=PlannerCommand(0.0, 0.0),
                next_state=RecoveryState.HOLDING,
                log_level='warn',
                log_message=(
                    f'Path found but front obstacle too close '
                    f'({front_obstacle_distance_m:.2f}m < {config.front_obstacle_threshold_m:.2f}m). '
                    f'Holding heading before reverse.'
                ),
                throttle_sec=1.0,
            )

        if current_state == RecoveryState.HOLDING:
            reverse_command = _reverse_command(config, obstacle_points_enu)
            return RecoveryDecision(
                command=reverse_command,
                next_state=RecoveryState.REVERSING,
                log_level='warn',
                log_message=(
                    f'Front obstacle still too close '
                    f'({front_obstacle_distance_m:.2f}m < {config.front_obstacle_threshold_m:.2f}m). '
                    f'Switching from HOLDING to REVERSING with escape yaw rate '
                    f'{reverse_command.yaw_rate_enu_rad_s:.3f} rad/s.'
                ),
                throttle_sec=1.0,
            )

    return RecoveryDecision(
        command=PlannerCommand(normal_speed_m_s, selected_yaw_rate_enu_rad_s),
        next_state=RecoveryState.NORMAL,
    )


def _decision_when_all_paths_blocked(
    front_obstacle_distance_m,
    current_state,
    config,
    obstacle_points_enu=None,
):
    """Handle recovery when every candidate arc is blocked.

    While every candidate path is blocked, do not exit REVERSING only because the
    front range is larger than clear_distance_m. The function itself means there
    is still no safe forward arc. Therefore, REVERSING continues until a path is
    actually found by the planner.
    """
    if current_state == RecoveryState.REVERSING:
        reverse_command = _reverse_command(config, obstacle_points_enu)
        return RecoveryDecision(
            command=reverse_command,
            next_state=RecoveryState.REVERSING,
            log_level='debug',
            log_message=(
                f'REVERSING: all paths still blocked. '
                f'Front obstacle distance: {front_obstacle_distance_m:.2f}m. '
                f'Escape yaw rate: {reverse_command.yaw_rate_enu_rad_s:.3f} rad/s.'
            ),
            throttle_sec=0.5,
        )

    if current_state == RecoveryState.NORMAL:
        return RecoveryDecision(
            command=PlannerCommand(0.0, 0.0),
            next_state=RecoveryState.HOLDING,
            log_level='warn',
            log_message=(
                f'All paths blocked. Holding before reverse. '
                f'Front obstacle distance: {front_obstacle_distance_m:.2f}m.'
            ),
            throttle_sec=2.0,
        )

    if current_state == RecoveryState.HOLDING:
        reverse_command = _reverse_command(config, obstacle_points_enu)
        return RecoveryDecision(
            command=reverse_command,
            next_state=RecoveryState.REVERSING,
            log_level='warn',
            log_message=(
                f'All paths still blocked after HOLDING. Switching to REVERSING. '
                f'Front obstacle distance: {front_obstacle_distance_m:.2f}m. '
                f'Escape yaw rate: {reverse_command.yaw_rate_enu_rad_s:.3f} rad/s.'
            ),
            throttle_sec=1.0,
        )

    return RecoveryDecision(
        command=PlannerCommand(0.0, 0.0),
        next_state=RecoveryState.HOLDING,
        log_level='warn',
        log_message='Unexpected recovery state while all paths blocked. Switching to HOLDING.',
        throttle_sec=2.0,
    )

