// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/ActuatorCommand.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ActuatorCommand in the package px4_msgs.
typedef struct px4_msgs__msg__ActuatorCommand
{
  /// time since system start
  uint64_t timestamp;
  double motor_pwm;
  double steering_pwm;
} px4_msgs__msg__ActuatorCommand;

// Struct for a sequence of px4_msgs__msg__ActuatorCommand.
typedef struct px4_msgs__msg__ActuatorCommand__Sequence
{
  px4_msgs__msg__ActuatorCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__ActuatorCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__STRUCT_H_
