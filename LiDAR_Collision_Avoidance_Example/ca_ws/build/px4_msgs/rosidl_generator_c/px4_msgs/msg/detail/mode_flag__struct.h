// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/ModeFlag.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__MODE_FLAG__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__MODE_FLAG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ModeFlag in the package px4_msgs.
typedef struct px4_msgs__msg__ModeFlag
{
  uint64_t timestamp;
  float modeone;
  float modetwo;
  float modethree;
  float modefour;
  float modefive;
  float modesix;
  float modeseven;
  float modeeight;
  float modenine;
  float modeten;
} px4_msgs__msg__ModeFlag;

// Struct for a sequence of px4_msgs__msg__ModeFlag.
typedef struct px4_msgs__msg__ModeFlag__Sequence
{
  px4_msgs__msg__ModeFlag * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__ModeFlag__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__MODE_FLAG__STRUCT_H_
