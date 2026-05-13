// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/command_values__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "px4_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "px4_msgs/msg/detail/command_values__struct.h"
#include "px4_msgs/msg/detail/command_values__functions.h"
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


using _CommandValues__ros_msg_type = px4_msgs__msg__CommandValues;

static bool _CommandValues__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _CommandValues__ros_msg_type * ros_message = static_cast<const _CommandValues__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: rc_on_off_log
  {
    cdr << ros_message->rc_on_off_log;
  }

  // Field name: d_mode_log
  {
    cdr << ros_message->d_mode_log;
  }

  // Field name: wp_mode_log
  {
    cdr << ros_message->wp_mode_log;
  }

  // Field name: u_cmd_log
  {
    cdr << ros_message->u_cmd_log;
  }

  // Field name: x_cmd_log
  {
    cdr << ros_message->x_cmd_log;
  }

  // Field name: y_cmd_log
  {
    cdr << ros_message->y_cmd_log;
  }

  // Field name: psi_cmd_log
  {
    cdr << ros_message->psi_cmd_log;
  }

  // Field name: ye_log
  {
    cdr << ros_message->ye_log;
  }

  // Field name: x_berth_start
  {
    cdr << ros_message->x_berth_start;
  }

  // Field name: y_berth_start
  {
    cdr << ros_message->y_berth_start;
  }

  // Field name: x_berth_end
  {
    cdr << ros_message->x_berth_end;
  }

  // Field name: y_berth_end
  {
    cdr << ros_message->y_berth_end;
  }

  return true;
}

static bool _CommandValues__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _CommandValues__ros_msg_type * ros_message = static_cast<_CommandValues__ros_msg_type *>(untyped_ros_message);
  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: rc_on_off_log
  {
    cdr >> ros_message->rc_on_off_log;
  }

  // Field name: d_mode_log
  {
    cdr >> ros_message->d_mode_log;
  }

  // Field name: wp_mode_log
  {
    cdr >> ros_message->wp_mode_log;
  }

  // Field name: u_cmd_log
  {
    cdr >> ros_message->u_cmd_log;
  }

  // Field name: x_cmd_log
  {
    cdr >> ros_message->x_cmd_log;
  }

  // Field name: y_cmd_log
  {
    cdr >> ros_message->y_cmd_log;
  }

  // Field name: psi_cmd_log
  {
    cdr >> ros_message->psi_cmd_log;
  }

  // Field name: ye_log
  {
    cdr >> ros_message->ye_log;
  }

  // Field name: x_berth_start
  {
    cdr >> ros_message->x_berth_start;
  }

  // Field name: y_berth_start
  {
    cdr >> ros_message->y_berth_start;
  }

  // Field name: x_berth_end
  {
    cdr >> ros_message->x_berth_end;
  }

  // Field name: y_berth_end
  {
    cdr >> ros_message->y_berth_end;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_px4_msgs
size_t get_serialized_size_px4_msgs__msg__CommandValues(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _CommandValues__ros_msg_type * ros_message = static_cast<const _CommandValues__ros_msg_type *>(untyped_ros_message);
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
  // field.name rc_on_off_log
  {
    size_t item_size = sizeof(ros_message->rc_on_off_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name d_mode_log
  {
    size_t item_size = sizeof(ros_message->d_mode_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name wp_mode_log
  {
    size_t item_size = sizeof(ros_message->wp_mode_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name u_cmd_log
  {
    size_t item_size = sizeof(ros_message->u_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x_cmd_log
  {
    size_t item_size = sizeof(ros_message->x_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y_cmd_log
  {
    size_t item_size = sizeof(ros_message->y_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name psi_cmd_log
  {
    size_t item_size = sizeof(ros_message->psi_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ye_log
  {
    size_t item_size = sizeof(ros_message->ye_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x_berth_start
  {
    size_t item_size = sizeof(ros_message->x_berth_start);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y_berth_start
  {
    size_t item_size = sizeof(ros_message->y_berth_start);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x_berth_end
  {
    size_t item_size = sizeof(ros_message->x_berth_end);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y_berth_end
  {
    size_t item_size = sizeof(ros_message->y_berth_end);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _CommandValues__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_px4_msgs__msg__CommandValues(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_px4_msgs
size_t max_serialized_size_px4_msgs__msg__CommandValues(
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
  // member: rc_on_off_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: d_mode_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: wp_mode_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: u_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: x_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: psi_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ye_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: x_berth_start
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y_berth_start
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: x_berth_end
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y_berth_end
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
    using DataType = px4_msgs__msg__CommandValues;
    is_plain =
      (
      offsetof(DataType, y_berth_end) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _CommandValues__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_px4_msgs__msg__CommandValues(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_CommandValues = {
  "px4_msgs::msg",
  "CommandValues",
  _CommandValues__cdr_serialize,
  _CommandValues__cdr_deserialize,
  _CommandValues__get_serialized_size,
  _CommandValues__max_serialized_size
};

static rosidl_message_type_support_t _CommandValues__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_CommandValues,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, px4_msgs, msg, CommandValues)() {
  return &_CommandValues__type_support;
}

#if defined(__cplusplus)
}
#endif
