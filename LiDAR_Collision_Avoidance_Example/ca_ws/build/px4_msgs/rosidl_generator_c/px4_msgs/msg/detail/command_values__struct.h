// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/CommandValues in the package px4_msgs.
typedef struct px4_msgs__msg__CommandValues
{
  uint64_t timestamp;
  float rc_on_off_log;
  float d_mode_log;
  float wp_mode_log;
  double u_cmd_log;
  double x_cmd_log;
  double y_cmd_log;
  double psi_cmd_log;
  double ye_log;
  double x_berth_start;
  double y_berth_start;
  double x_berth_end;
  double y_berth_end;
} px4_msgs__msg__CommandValues;

// Struct for a sequence of px4_msgs__msg__CommandValues.
typedef struct px4_msgs__msg__CommandValues__Sequence
{
  px4_msgs__msg__CommandValues * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__CommandValues__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__STRUCT_H_
