// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/states_and_actuators__rosidl_typesupport_fastrtps_cpp.hpp"
#include "px4_msgs/msg/detail/states_and_actuators__struct.hpp"

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
  const px4_msgs::msg::StatesAndActuators & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: timestamp
  cdr << ros_message.timestamp;
  // Member: u_time_log
  cdr << ros_message.u_time_log;
  // Member: v_time_log
  cdr << ros_message.v_time_log;
  // Member: r_time_log
  cdr << ros_message.r_time_log;
  // Member: x_time_log
  cdr << ros_message.x_time_log;
  // Member: y_time_log
  cdr << ros_message.y_time_log;
  // Member: psi_time_log
  cdr << ros_message.psi_time_log;
  // Member: taux_time_log
  cdr << ros_message.taux_time_log;
  // Member: tauy_time_log
  cdr << ros_message.tauy_time_log;
  // Member: taun_time_log
  cdr << ros_message.taun_time_log;
  // Member: motor1_time_log
  cdr << ros_message.motor1_time_log;
  // Member: motor2_time_log
  cdr << ros_message.motor2_time_log;
  // Member: motor3_time_log
  cdr << ros_message.motor3_time_log;
  // Member: motor4_time_log
  cdr << ros_message.motor4_time_log;
  // Member: alpha1_time_log
  cdr << ros_message.alpha1_time_log;
  // Member: alpha2_time_log
  cdr << ros_message.alpha2_time_log;
  // Member: alpha3_time_log
  cdr << ros_message.alpha3_time_log;
  // Member: alpha4_time_log
  cdr << ros_message.alpha4_time_log;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  px4_msgs::msg::StatesAndActuators & ros_message)
{
  // Member: timestamp
  cdr >> ros_message.timestamp;

  // Member: u_time_log
  cdr >> ros_message.u_time_log;

  // Member: v_time_log
  cdr >> ros_message.v_time_log;

  // Member: r_time_log
  cdr >> ros_message.r_time_log;

  // Member: x_time_log
  cdr >> ros_message.x_time_log;

  // Member: y_time_log
  cdr >> ros_message.y_time_log;

  // Member: psi_time_log
  cdr >> ros_message.psi_time_log;

  // Member: taux_time_log
  cdr >> ros_message.taux_time_log;

  // Member: tauy_time_log
  cdr >> ros_message.tauy_time_log;

  // Member: taun_time_log
  cdr >> ros_message.taun_time_log;

  // Member: motor1_time_log
  cdr >> ros_message.motor1_time_log;

  // Member: motor2_time_log
  cdr >> ros_message.motor2_time_log;

  // Member: motor3_time_log
  cdr >> ros_message.motor3_time_log;

  // Member: motor4_time_log
  cdr >> ros_message.motor4_time_log;

  // Member: alpha1_time_log
  cdr >> ros_message.alpha1_time_log;

  // Member: alpha2_time_log
  cdr >> ros_message.alpha2_time_log;

  // Member: alpha3_time_log
  cdr >> ros_message.alpha3_time_log;

  // Member: alpha4_time_log
  cdr >> ros_message.alpha4_time_log;

  return true;
}  // NOLINT(readability/fn_size)

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
get_serialized_size(
  const px4_msgs::msg::StatesAndActuators & ros_message,
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
  // Member: u_time_log
  {
    size_t item_size = sizeof(ros_message.u_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: v_time_log
  {
    size_t item_size = sizeof(ros_message.v_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: r_time_log
  {
    size_t item_size = sizeof(ros_message.r_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x_time_log
  {
    size_t item_size = sizeof(ros_message.x_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y_time_log
  {
    size_t item_size = sizeof(ros_message.y_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: psi_time_log
  {
    size_t item_size = sizeof(ros_message.psi_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: taux_time_log
  {
    size_t item_size = sizeof(ros_message.taux_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: tauy_time_log
  {
    size_t item_size = sizeof(ros_message.tauy_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: taun_time_log
  {
    size_t item_size = sizeof(ros_message.taun_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: motor1_time_log
  {
    size_t item_size = sizeof(ros_message.motor1_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: motor2_time_log
  {
    size_t item_size = sizeof(ros_message.motor2_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: motor3_time_log
  {
    size_t item_size = sizeof(ros_message.motor3_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: motor4_time_log
  {
    size_t item_size = sizeof(ros_message.motor4_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: alpha1_time_log
  {
    size_t item_size = sizeof(ros_message.alpha1_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: alpha2_time_log
  {
    size_t item_size = sizeof(ros_message.alpha2_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: alpha3_time_log
  {
    size_t item_size = sizeof(ros_message.alpha3_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: alpha4_time_log
  {
    size_t item_size = sizeof(ros_message.alpha4_time_log);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_px4_msgs
max_serialized_size_StatesAndActuators(
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

  // Member: u_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: v_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: r_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: x_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: y_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: psi_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: taux_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: tauy_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: taun_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: motor1_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: motor2_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: motor3_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: motor4_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: alpha1_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: alpha2_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: alpha3_time_log
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: alpha4_time_log
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
    using DataType = px4_msgs::msg::StatesAndActuators;
    is_plain =
      (
      offsetof(DataType, alpha4_time_log) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _StatesAndActuators__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const px4_msgs::msg::StatesAndActuators *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _StatesAndActuators__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<px4_msgs::msg::StatesAndActuators *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _StatesAndActuators__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const px4_msgs::msg::StatesAndActuators *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _StatesAndActuators__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_StatesAndActuators(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _StatesAndActuators__callbacks = {
  "px4_msgs::msg",
  "StatesAndActuators",
  _StatesAndActuators__cdr_serialize,
  _StatesAndActuators__cdr_deserialize,
  _StatesAndActuators__get_serialized_size,
  _StatesAndActuators__max_serialized_size
};

static rosidl_message_type_support_t _StatesAndActuators__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_StatesAndActuators__callbacks,
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
get_message_type_support_handle<px4_msgs::msg::StatesAndActuators>()
{
  return &px4_msgs::msg::typesupport_fastrtps_cpp::_StatesAndActuators__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, px4_msgs, msg, StatesAndActuators)() {
  return &px4_msgs::msg::typesupport_fastrtps_cpp::_StatesAndActuators__handle;
}

#ifdef __cplusplus
}
#endif
