// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from px4_msgs:msg/OutputTest.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "px4_msgs/msg/detail/output_test__rosidl_typesupport_introspection_c.h"
#include "px4_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "px4_msgs/msg/detail/output_test__functions.h"
#include "px4_msgs/msg/detail/output_test__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  px4_msgs__msg__OutputTest__init(message_memory);
}

void px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_fini_function(void * message_memory)
{
  px4_msgs__msg__OutputTest__fini(message_memory);
}

size_t px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__size_function__OutputTest__sates(
  const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_const_function__OutputTest__sates(
  const void * untyped_member, size_t index)
{
  const double * member =
    (const double *)(untyped_member);
  return &member[index];
}

void * px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_function__OutputTest__sates(
  void * untyped_member, size_t index)
{
  double * member =
    (double *)(untyped_member);
  return &member[index];
}

void px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__fetch_function__OutputTest__sates(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_const_function__OutputTest__sates(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__assign_function__OutputTest__sates(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_function__OutputTest__sates(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

size_t px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__size_function__OutputTest__command(
  const void * untyped_member)
{
  (void)untyped_member;
  return 7;
}

const void * px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_const_function__OutputTest__command(
  const void * untyped_member, size_t index)
{
  const double * member =
    (const double *)(untyped_member);
  return &member[index];
}

void * px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_function__OutputTest__command(
  void * untyped_member, size_t index)
{
  double * member =
    (double *)(untyped_member);
  return &member[index];
}

void px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__fetch_function__OutputTest__command(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_const_function__OutputTest__command(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__assign_function__OutputTest__command(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_function__OutputTest__command(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_member_array[8] = {
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "timestamp_last_signal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, timestamp_last_signal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sates",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, sates),  // bytes offset in struct
    NULL,  // default value
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__size_function__OutputTest__sates,  // size() function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_const_function__OutputTest__sates,  // get_const(index) function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_function__OutputTest__sates,  // get(index) function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__fetch_function__OutputTest__sates,  // fetch(index, &value) function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__assign_function__OutputTest__sates,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    7,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, command),  // bytes offset in struct
    NULL,  // default value
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__size_function__OutputTest__command,  // size() function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_const_function__OutputTest__command,  // get_const(index) function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__get_function__OutputTest__command,  // get(index) function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__fetch_function__OutputTest__command,  // fetch(index, &value) function pointer
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__assign_function__OutputTest__command,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "estimated_d",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, estimated_d),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "eso_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, eso_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "nomoto_t",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, nomoto_t),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "nomoto_k",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(px4_msgs__msg__OutputTest, nomoto_k),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_members = {
  "px4_msgs__msg",  // message namespace
  "OutputTest",  // message name
  8,  // number of fields
  sizeof(px4_msgs__msg__OutputTest),
  px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_member_array,  // message members
  px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_init_function,  // function to initialize message memory (memory has to be allocated)
  px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_type_support_handle = {
  0,
  &px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_px4_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, px4_msgs, msg, OutputTest)() {
  if (!px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_type_support_handle.typesupport_identifier) {
    px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &px4_msgs__msg__OutputTest__rosidl_typesupport_introspection_c__OutputTest_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
