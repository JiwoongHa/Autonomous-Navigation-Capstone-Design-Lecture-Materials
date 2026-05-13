// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/InputTau.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__INPUT_TAU__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__INPUT_TAU__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/InputTau in the package px4_msgs.
typedef struct px4_msgs__msg__InputTau
{
  /// time since system start (microseconds)
  uint64_t timestamp;
  /// last valid reception time
  uint64_t timestamp_last_signal;
  /// number of channels actually being seen
  uint8_t channel_count;
  /// docking method(1.sway,2.front,3.NED frame,4.SMC)
  int8_t docking_type;
  /// waypoint following guidance algorithm(0.actangent, 1.LOS)
  int8_t wp_guid;
  /// docking guidance algorithm(0.actangent, 1.LOS)
  int8_t docking_guid;
  /// docking start and final x position
  double dock_x[2];
  /// docking start and final y position
  double dock_y[2];
  /// operation method(0.Waypoint, 1.Berthing)
  int8_t operation_type;
  /// waypoint following and docking crosstrck error
  double ye;
  /// USV pos data (x(m), y(m), psi(rad)) in NED frame
  double pos[3];
  /// Input source (RC or Auto)
  uint8_t input_source;
  /// tau(Fx, Fy, N)
  double tau[3];
} px4_msgs__msg__InputTau;

// Struct for a sequence of px4_msgs__msg__InputTau.
typedef struct px4_msgs__msg__InputTau__Sequence
{
  px4_msgs__msg__InputTau * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__InputTau__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__INPUT_TAU__STRUCT_H_
