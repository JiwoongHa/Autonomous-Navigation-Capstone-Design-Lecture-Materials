// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/StatesAndActuators in the package px4_msgs.
typedef struct px4_msgs__msg__StatesAndActuators
{
  uint64_t timestamp;
  double u_time_log;
  double v_time_log;
  double r_time_log;
  double x_time_log;
  double y_time_log;
  double psi_time_log;
  double taux_time_log;
  double tauy_time_log;
  double taun_time_log;
  double motor1_time_log;
  double motor2_time_log;
  double motor3_time_log;
  double motor4_time_log;
  double alpha1_time_log;
  double alpha2_time_log;
  double alpha3_time_log;
  double alpha4_time_log;
} px4_msgs__msg__StatesAndActuators;

// Struct for a sequence of px4_msgs__msg__StatesAndActuators.
typedef struct px4_msgs__msg__StatesAndActuators__Sequence
{
  px4_msgs__msg__StatesAndActuators * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__StatesAndActuators__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__STRUCT_H_
