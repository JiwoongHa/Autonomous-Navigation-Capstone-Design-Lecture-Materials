// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/command_values__rosidl_typesupport_fastrtps_cpp.hpp"
#include "px4_msgs/msg/detail/command_values__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace px4_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
cdr_serialize(
  const px4_msgs::msg::CommandValues & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: timestamp
  cdr << ros_message.timestamp;
  // Member: rc_on_off_log
  cdr << ros_message.rc_on_off_log;
  // Member: d_mode_log
  cdr << ros_message.d_mode_log;
  // Member: wp_mode_log
  cdr << ros_message.wp_mode_log;
  // Member: u_cmd_log
  cdr << ros_message.u_cmd_log;
  // Member: x_cmd_log
  cdr << ros_message.x_cmd_log;
  // Member: y_cmd_log
  cdr << ros_message.y_cmd_log;
  // Member: psi_cmd_log
  cdr << ros_message.psi_cmd_log;
  // Member: ye_log
  cdr << ros_message.ye_log;
  // Member: x_berth_start
  cdr << ros_message.x_berth_start;
  // Member: y_berth_start
  cdr << ros_message.y_berth_start;
  // Member: x_berth_end
  cdr << ros_message.x_berth_end;
  // Member: y_berth_end
  cdr << ros_message.y_berth_end;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  px4_msgs::msg::CommandValues & ros_message)
{
  // Member: timestamp
  cdr >> ros_message.timestamp;

  // Member: rc_on_off_log
  cdr >> ros_message.rc_on_off_log;

  // Member: d_mode_log
  cdr >> ros_message.d_mode_log;

  // Member: wp_mode_log
  cdr >> ros_message.wp_mode_log;

  // Member: u_cmd_log
  cdr >> ros_message.u_cmd_log;

  // Member: x_cmd_log
  cdr >> ros_message.x_cmd_log;

  // Member: y_cmd_log
  cdr >> ros_message.y_cmd_log;

  // Member: psi_cmd_log
  cdr >> ros_message.psi_cmd_log;

  // Member: ye_log
  cdr >> ros_message.ye_log;

  // Member: x_berth_start
  cdr >> ros_message.x_berth_start;

  // Member: y_berth_start
  cdr >> ros_message.y_berth_start;

  // Member: x_berth_end
  cdr >> ros_message.x_berth_end;

  // Member: y_berth_end
  cdr >> ros_message.y_berth_end;

  return true;
}  // NOLINT(readability/fn_size)

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
get_serialized_size(
  const px4_msgs::msg::CommandValues & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: timestamp
  {
    size_t item_size = sizeof(ros_message.timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: rc_on_off_log
  {
    size_t item_size = sizeof(ros_message.rc_on_off_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: d_mode_log
  {
    size_t item_size = sizeof(ros_message.d_mode_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: wp_mode_log
  {
    size_t item_size = sizeof(ros_message.wp_mode_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: u_cmd_log
  {
    size_t item_size = sizeof(ros_message.u_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x_cmd_log
  {
    size_t item_size = sizeof(ros_message.x_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y_cmd_log
  {
    size_t item_size = sizeof(ros_message.y_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: psi_cmd_log
  {
    size_t item_size = sizeof(ros_message.psi_cmd_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ye_log
  {
    size_t item_size = sizeof(ros_message.ye_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x_berth_start
  {
    size_t item_size = sizeof(ros_message.x_berth_start);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y_berth_start
  {
    size_t item_size = sizeof(ros_message.y_berth_start);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x_berth_end
  {
    size_t item_size = sizeof(ros_message.x_berth_end);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y_berth_end
  {
    size_t item_size = sizeof(ros_message.y_berth_end);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
max_serialized_size_CommandValues(
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


  // Member: timestamp
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: rc_on_off_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: d_mode_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: wp_mode_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: u_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: x_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: y_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: psi_cmd_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: ye_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: x_berth_start
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: y_berth_start
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: x_berth_end
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: y_berth_end
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
    using DataType = px4_msgs::msg::CommandValues;
    is_plain =
      (
      offsetof(DataType, y_berth_end) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _CommandValues__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const px4_msgs::msg::CommandValues *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _CommandValues__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<px4_msgs::msg::CommandValues *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _CommandValues__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const px4_msgs::msg::CommandValues *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _CommandValues__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_CommandValues(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _CommandValues__callbacks = {
  "px4_msgs::msg",
  "CommandValues",
  _CommandValues__cdr_serialize,
  _CommandValues__cdr_deserialize,
  _CommandValues__get_serialized_size,
  _CommandValues__max_serialized_size
};

static rosidl_message_type_support_t _CommandValues__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_CommandValues__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace px4_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_px4_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<px4_msgs::msg::CommandValues>()
{
  return &px4_msgs::msg::typesupport_fastrtps_cpp::_CommandValues__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, px4_msgs, msg, CommandValues)() {
  return &px4_msgs::msg::typesupport_fastrtps_cpp::_CommandValues__handle;
}

#ifdef __cplusplus
}
#endif
