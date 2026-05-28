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
            )

        return _decision_when_all_paths_blocked(
            front_obstacle_distance_m=front_obstacle_distance_m,
            current_state=current_state,
            config=config,
        )


def normalize_recovery_state(state):
    """Convert strings or enum values to RecoveryState."""
    if isinstance(state, RecoveryState):
        return state
    try:
        return RecoveryState(str(state))
    except ValueError:
        return RecoveryState.NORMAL


def scan_to_obstacle_data(
    ranges,
    angle_min,
    angle_max,
    ignore_radius_m,
    max_lookahead_m,
    front_angle_rad,
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


def _decision_when_path_found(
    selected_yaw_rate_enu_rad_s,
    normal_speed_m_s,
    front_obstacle_distance_m,
    current_state,
    config,
):
    """Handle recovery while a non-colliding arc exists.

    State transition policy:
    - NORMAL + close front obstacle  -> HOLDING for one control cycle
    - HOLDING + close front obstacle -> REVERSING
    - REVERSING continues until the front distance reaches clear_distance_m
    - clear front distance           -> NORMAL
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
        return RecoveryDecision(
            command=PlannerCommand(config.reverse_speed_m_s, 0.0),
            next_state=RecoveryState.REVERSING,
            log_level='debug',
            log_message=(
                f'REVERSING: front obstacle {front_obstacle_distance_m:.2f}m. '
                f'Continuing reverse until {config.clear_distance_m:.2f}m clear distance.'
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
            return RecoveryDecision(
                command=PlannerCommand(config.reverse_speed_m_s, 0.0),
                next_state=RecoveryState.REVERSING,
                log_level='warn',
                log_message=(
                    f'Front obstacle still too close '
                    f'({front_obstacle_distance_m:.2f}m < {config.front_obstacle_threshold_m:.2f}m). '
                    f'Switching from HOLDING to REVERSING.'
                ),
                throttle_sec=1.0,
            )

    return RecoveryDecision(
        command=PlannerCommand(normal_speed_m_s, selected_yaw_rate_enu_rad_s),
        next_state=RecoveryState.NORMAL,
    )


def _decision_when_all_paths_blocked(front_obstacle_distance_m, current_state, config):
    """Handle recovery when every candidate arc is blocked."""
    if current_state == RecoveryState.REVERSING:
        if front_obstacle_distance_m >= config.clear_distance_m:
            return RecoveryDecision(
                command=PlannerCommand(0.0, 0.0),
                next_state=RecoveryState.HOLDING,
                log_level='info',
                log_message=(
                    f'Front cleared ({front_obstacle_distance_m:.2f}m >= '
                    f'{config.clear_distance_m:.2f}m). Stopping reverse and holding.'
                ),
                throttle_sec=1.0,
            )

        return RecoveryDecision(
            command=PlannerCommand(config.reverse_speed_m_s, 0.0),
            next_state=RecoveryState.REVERSING,
            log_level='debug',
            log_message=(
                f'REVERSING: front obstacle {front_obstacle_distance_m:.2f}m. '
                f'Continuing reverse until {config.clear_distance_m:.2f}m clear distance.'
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
                    f'All paths blocked. Front obstacle too close '
                    f'({front_obstacle_distance_m:.2f}m < {config.front_obstacle_threshold_m:.2f}m). '
                    f'Holding heading before reverse.'
                ),
                throttle_sec=2.0,
            )

        if current_state == RecoveryState.HOLDING:
            return RecoveryDecision(
                command=PlannerCommand(config.reverse_speed_m_s, 0.0),
                next_state=RecoveryState.REVERSING,
                log_level='warn',
                log_message=(
                    f'All paths still blocked and front obstacle remains too close '
                    f'({front_obstacle_distance_m:.2f}m < {config.front_obstacle_threshold_m:.2f}m). '
                    f'Switching from HOLDING to REVERSING.'
                ),
                throttle_sec=1.0,
            )

    return RecoveryDecision(
        command=PlannerCommand(0.0, 0.0),
        next_state=RecoveryState.NORMAL,
        log_level='warn',
        log_message=(
            f'All paths blocked but front clear ({front_obstacle_distance_m:.2f}m). Waiting.'
        ),
        throttle_sec=2.0,
    )


def _command_for_blocked_front(state, config):
    if state == RecoveryState.REVERSING:
        return PlannerCommand(config.reverse_speed_m_s, 0.0)
    return PlannerCommand(0.0, 0.0)
