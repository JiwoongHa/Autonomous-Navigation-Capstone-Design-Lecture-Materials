// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4_msgs:msg/SimulinkCustomMessage.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__TRAITS_HPP_
#define PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4_msgs/msg/detail/simulink_custom_message__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const SimulinkCustomMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: single_a
  {
    out << "single_a: ";
    rosidl_generator_traits::value_to_yaml(msg.single_a, out);
    out << ", ";
  }

  // member: single_b
  {
    out << "single_b: ";
    rosidl_generator_traits::value_to_yaml(msg.single_b, out);
    out << ", ";
  }

  // member: double_a
  {
    out << "double_a: ";
    rosidl_generator_traits::value_to_yaml(msg.double_a, out);
    out << ", ";
  }

  // member: double_b
  {
    out << "double_b: ";
    rosidl_generator_traits::value_to_yaml(msg.double_b, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SimulinkCustomMessage & msg,
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

  // member: single_a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "single_a: ";
    rosidl_generator_traits::value_to_yaml(msg.single_a, out);
    out << "\n";
  }

  // member: single_b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "single_b: ";
    rosidl_generator_traits::value_to_yaml(msg.single_b, out);
    out << "\n";
  }

  // member: double_a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "double_a: ";
    rosidl_generator_traits::value_to_yaml(msg.double_a, out);
    out << "\n";
  }

  // member: double_b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "double_b: ";
    rosidl_generator_traits::value_to_yaml(msg.double_b, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SimulinkCustomMessage & msg, bool use_flow_style = false)
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
  const px4_msgs::msg::SimulinkCustomMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4_msgs::msg::SimulinkCustomMessage & msg)
{
  return px4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4_msgs::msg::SimulinkCustomMessage>()
{
  return "px4_msgs::msg::SimulinkCustomMessage";
}

template<>
inline const char * name<px4_msgs::msg::SimulinkCustomMessage>()
{
  return "px4_msgs/msg/SimulinkCustomMessage";
}

template<>
struct has_fixed_size<px4_msgs::msg::SimulinkCustomMessage>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4_msgs::msg::SimulinkCustomMessage>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4_msgs::msg::SimulinkCustomMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__TRAITS_HPP_
