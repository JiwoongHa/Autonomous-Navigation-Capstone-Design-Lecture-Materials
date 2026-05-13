// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/states_and_actuators__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "px4_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "px4_msgs/msg/detail/states_and_actuators__struct.h"
#include "px4_msgs/msg/detail/states_and_actuators__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _StatesAndActuators__ros_msg_type = px4_msgs__msg__StatesAndActuators;

static bool _StatesAndActuators__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _StatesAndActuators__ros_msg_type * ros_message = static_cast<const _StatesAndActuators__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: u_time_log
  {
    cdr << ros_message->u_time_log;
  }

  // Field name: v_time_log
  {
    cdr << ros_message->v_time_log;
  }

  // Field name: r_time_log
  {
    cdr << ros_message->r_time_log;
  }

  // Field name: x_time_log
  {
    cdr << ros_message->x_time_log;
  }

  // Field name: y_time_log
  {
    cdr << ros_message->y_time_log;
  }

  // Field name: psi_time_log
  {
    cdr << ros_message->psi_time_log;
  }

  // Field name: taux_time_log
  {
    cdr << ros_message->taux_time_log;
  }

  // Field name: tauy_time_log
  {
    cdr << ros_message->tauy_time_log;
  }

  // Field name: taun_time_log
  {
    cdr << ros_message->taun_time_log;
  }

  // Field name: motor1_time_log
  {
    cdr << ros_message->motor1_time_log;
  }

  // Field name: motor2_time_log
  {
    cdr << ros_message->motor2_time_log;
  }

  // Field name: motor3_time_log
  {
    cdr << ros_message->motor3_time_log;
  }

  // Field name: motor4_time_log
  {
    cdr << ros_message->motor4_time_log;
  }

  // Field name: alpha1_time_log
  {
    cdr << ros_message->alpha1_time_log;
  }

  // Field name: alpha2_time_log
  {
    cdr << ros_message->alpha2_time_log;
  }

  // Field name: alpha3_time_log
  {
    cdr << ros_message->alpha3_time_log;
  }

  // Field name: alpha4_time_log
  {
    cdr << ros_message->alpha4_time_log;
  }

  return true;
}

static bool _StatesAndActuators__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _StatesAndActuators__ros_msg_type * ros_message = static_cast<_StatesAndActuators__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: u_time_log
  {
    cdr >> ros_message->u_time_log;
  }

  // Field name: v_time_log
  {
    cdr >> ros_message->v_time_log;
  }

  // Field name: r_time_log
  {
    cdr >> ros_message->r_time_log;
  }

  // Field name: x_time_log
  {
    cdr >> ros_message->x_time_log;
  }

  // Field name: y_time_log
  {
    cdr >> ros_message->y_time_log;
  }

  // Field name: psi_time_log
  {
    cdr >> ros_message->psi_time_log;
  }

  // Field name: taux_time_log
  {
    cdr >> ros_message->taux_time_log;
  }

  // Field name: tauy_time_log
  {
    cdr >> ros_message->tauy_time_log;
  }

  // Field name: taun_time_log
  {
    cdr >> ros_message->taun_time_log;
  }

  // Field name: motor1_time_log
  {
    cdr >> ros_message->motor1_time_log;
  }

  // Field name: motor2_time_log
  {
    cdr >> ros_message->motor2_time_log;
  }

  // Field name: motor3_time_log
  {
    cdr >> ros_message->motor3_time_log;
  }

  // Field name: motor4_time_log
  {
    cdr >> ros_message->motor4_time_log;
  }

  // Field name: alpha1_time_log
  {
    cdr >> ros_message->alpha1_time_log;
  }

  // Field name: alpha2_time_log
  {
    cdr >> ros_message->alpha2_time_log;
  }

  // Field name: alpha3_time_log
  {
    cdr >> ros_message->alpha3_time_log;
  }

  // Field name: alpha4_time_log
  {
    cdr >> ros_message->alpha4_time_log;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_px4_msgs
size_t get_serialized_size_px4_msgs__msg__StatesAndActuators(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _StatesAndActuators__ros_msg_type * ros_message = static_cast<const _StatesAndActuators__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name timestamp
  {
    size_t item_size = sizeof(ros_message->timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name u_time_log
  {
    size_t item_size = sizeof(ros_message->u_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name v_time_log
  {
    size_t item_size = sizeof(ros_message->v_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name r_time_log
  {
    size_t item_size = sizeof(ros_message->r_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x_time_log
  {
    size_t item_size = sizeof(ros_message->x_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y_time_log
  {
    size_t item_size = sizeof(ros_message->y_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name psi_time_log
  {
    size_t item_size = sizeof(ros_message->psi_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name taux_time_log
  {
    size_t item_size = sizeof(ros_message->taux_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tauy_time_log
  {
    size_t item_size = sizeof(ros_message->tauy_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name taun_time_log
  {
    size_t item_size = sizeof(ros_message->taun_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name motor1_time_log
  {
    size_t item_size = sizeof(ros_message->motor1_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name motor2_time_log
  {
    size_t item_size = sizeof(ros_message->motor2_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name motor3_time_log
  {
    size_t item_size = sizeof(ros_message->motor3_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name motor4_time_log
  {
    size_t item_size = sizeof(ros_message->motor4_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alpha1_time_log
  {
    size_t item_size = sizeof(ros_message->alpha1_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alpha2_time_log
  {
    size_t item_size = sizeof(ros_message->alpha2_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alpha3_time_log
  {
    size_t item_size = sizeof(ros_message->alpha3_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alpha4_time_log
  {
    size_t item_size = sizeof(ros_message->alpha4_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _StatesAndActuators__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_px4_msgs__msg__StatesAndActuators(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_px4_msgs
size_t max_serialized_size_px4_msgs__msg__StatesAndActuators(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: timestamp
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: u_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: v_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: r_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: x_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: psi_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: taux_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: tauy_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: taun_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: motor1_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: motor2_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: motor3_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: motor4_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alpha1_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alpha2_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alpha3_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alpha4_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = px4_msgs__msg__StatesAndActuators;
    is_plain =
      (
      offsetof(DataType, alpha4_time_log) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _StatesAndActuators__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_px4_msgs__msg__StatesAndActuators(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_StatesAndActuators = {
  "px4_msgs::msg",
  "StatesAndActuators",
  _StatesAndActuators__cdr_serialize,
  _StatesAndActuators__cdr_deserialize,
  _StatesAndActuators__get_serialized_size,
  _StatesAndActuators__max_serialized_size
};

static rosidl_message_type_support_t _StatesAndActuators__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_StatesAndActuators,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, px4_msgs, msg, StatesAndActuators)() {
  return &_StatesAndActuators__type_support;
}

#if defined(__cplusplus)
}
#endif
