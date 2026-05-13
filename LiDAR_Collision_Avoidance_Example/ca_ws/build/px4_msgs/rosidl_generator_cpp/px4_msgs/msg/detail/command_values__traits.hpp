// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__TRAITS_HPP_
#define PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4_msgs/msg/detail/command_values__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CommandValues & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: rc_on_off_log
  {
    out << "rc_on_off_log: ";
    rosidl_generator_traits::value_to_yaml(msg.rc_on_off_log, out);
    out << ", ";
  }

  // member: d_mode_log
  {
    out << "d_mode_log: ";
    rosidl_generator_traits::value_to_yaml(msg.d_mode_log, out);
    out << ", ";
  }

  // member: wp_mode_log
  {
    out << "wp_mode_log: ";
    rosidl_generator_traits::value_to_yaml(msg.wp_mode_log, out);
    out << ", ";
  }

  // member: u_cmd_log
  {
    out << "u_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.u_cmd_log, out);
    out << ", ";
  }

  // member: x_cmd_log
  {
    out << "x_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.x_cmd_log, out);
    out << ", ";
  }

  // member: y_cmd_log
  {
    out << "y_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.y_cmd_log, out);
    out << ", ";
  }

  // member: psi_cmd_log
  {
    out << "psi_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.psi_cmd_log, out);
    out << ", ";
  }

  // member: ye_log
  {
    out << "ye_log: ";
    rosidl_generator_traits::value_to_yaml(msg.ye_log, out);
    out << ", ";
  }

  // member: x_berth_start
  {
    out << "x_berth_start: ";
    rosidl_generator_traits::value_to_yaml(msg.x_berth_start, out);
    out << ", ";
  }

  // member: y_berth_start
  {
    out << "y_berth_start: ";
    rosidl_generator_traits::value_to_yaml(msg.y_berth_start, out);
    out << ", ";
  }

  // member: x_berth_end
  {
    out << "x_berth_end: ";
    rosidl_generator_traits::value_to_yaml(msg.x_berth_end, out);
    out << ", ";
  }

  // member: y_berth_end
  {
    out << "y_berth_end: ";
    rosidl_generator_traits::value_to_yaml(msg.y_berth_end, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CommandValues & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << "\n";
  }

  // member: rc_on_off_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rc_on_off_log: ";
    rosidl_generator_traits::value_to_yaml(msg.rc_on_off_log, out);
    out << "\n";
  }

  // member: d_mode_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "d_mode_log: ";
    rosidl_generator_traits::value_to_yaml(msg.d_mode_log, out);
    out << "\n";
  }

  // member: wp_mode_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wp_mode_log: ";
    rosidl_generator_traits::value_to_yaml(msg.wp_mode_log, out);
    out << "\n";
  }

  // member: u_cmd_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "u_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.u_cmd_log, out);
    out << "\n";
  }

  // member: x_cmd_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.x_cmd_log, out);
    out << "\n";
  }

  // member: y_cmd_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.y_cmd_log, out);
    out << "\n";
  }

  // member: psi_cmd_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "psi_cmd_log: ";
    rosidl_generator_traits::value_to_yaml(msg.psi_cmd_log, out);
    out << "\n";
  }

  // member: ye_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ye_log: ";
    rosidl_generator_traits::value_to_yaml(msg.ye_log, out);
    out << "\n";
  }

  // member: x_berth_start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_berth_start: ";
    rosidl_generator_traits::value_to_yaml(msg.x_berth_start, out);
    out << "\n";
  }

  // member: y_berth_start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_berth_start: ";
    rosidl_generator_traits::value_to_yaml(msg.y_berth_start, out);
    out << "\n";
  }

  // member: x_berth_end
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_berth_end: ";
    rosidl_generator_traits::value_to_yaml(msg.x_berth_end, out);
    out << "\n";
  }

  // member: y_berth_end
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_berth_end: ";
    rosidl_generator_traits::value_to_yaml(msg.y_berth_end, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CommandValues & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace px4_msgs

namespace rosidl_generator_traits
{

[[deprecated("use px4_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const px4_msgs::msg::CommandValues & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4_msgs::msg::CommandValues & msg)
{
  return px4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4_msgs::msg::CommandValues>()
{
  return "px4_msgs::msg::CommandValues";
}

template<>
inline const char * name<px4_msgs::msg::CommandValues>()
{
  return "px4_msgs/msg/CommandValues";
}

template<>
struct has_fixed_size<px4_msgs::msg::CommandValues>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4_msgs::msg::CommandValues>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4_msgs::msg::CommandValues>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__TRAITS_HPP_
