// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/OutputTest.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/OutputTest in the package px4_msgs.
typedef struct px4_msgs__msg__OutputTest
{
  /// time since system start (microseconds)
  uint64_t timestamp;
  /// last valid reception time
  uint64_t timestamp_last_signal;
  /// States(u;v;w;p;q;r;x;y;psi)
  double sates[9];
  /// Command(u_cmd; psi_cmd; wp_mode; ye; d_pos_x; d_pos_y; d_psi;)
  double command[7];
  /// estimated disturbance about N using ESO
  double estimated_d;
  /// ESO enabled(0.disabled, 1.enabled)
  int8_t eso_type;
  /// Nomoto model T value
  float nomoto_t;
  /// Nomoto model k value
  float nomoto_k;
} px4_msgs__msg__OutputTest;

// Struct for a sequence of px4_msgs__msg__OutputTest.
typedef struct px4_msgs__msg__OutputTest__Sequence
{
  px4_msgs__msg__OutputTest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__OutputTest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__STRUCT_H_
