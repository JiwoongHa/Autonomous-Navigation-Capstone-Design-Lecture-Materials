// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4_msgs:msg/ModeFlag.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__MODE_FLAG__TRAITS_HPP_
#define PX4_MSGS__MSG__DETAIL__MODE_FLAG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4_msgs/msg/detail/mode_flag__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ModeFlag & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: modeone
  {
    out << "modeone: ";
    rosidl_generator_traits::value_to_yaml(msg.modeone, out);
    out << ", ";
  }

  // member: modetwo
  {
    out << "modetwo: ";
    rosidl_generator_traits::value_to_yaml(msg.modetwo, out);
    out << ", ";
  }

  // member: modethree
  {
    out << "modethree: ";
    rosidl_generator_traits::value_to_yaml(msg.modethree, out);
    out << ", ";
  }

  // member: modefour
  {
    out << "modefour: ";
    rosidl_generator_traits::value_to_yaml(msg.modefour, out);
    out << ", ";
  }

  // member: modefive
  {
    out << "modefive: ";
    rosidl_generator_traits::value_to_yaml(msg.modefive, out);
    out << ", ";
  }

  // member: modesix
  {
    out << "modesix: ";
    rosidl_generator_traits::value_to_yaml(msg.modesix, out);
    out << ", ";
  }

  // member: modeseven
  {
    out << "modeseven: ";
    rosidl_generator_traits::value_to_yaml(msg.modeseven, out);
    out << ", ";
  }

  // member: modeeight
  {
    out << "modeeight: ";
    rosidl_generator_traits::value_to_yaml(msg.modeeight, out);
    out << ", ";
  }

  // member: modenine
  {
    out << "modenine: ";
    rosidl_generator_traits::value_to_yaml(msg.modenine, out);
    out << ", ";
  }

  // member: modeten
  {
    out << "modeten: ";
    rosidl_generator_traits::value_to_yaml(msg.modeten, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ModeFlag & msg,
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

  // member: modeone
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modeone: ";
    rosidl_generator_traits::value_to_yaml(msg.modeone, out);
    out << "\n";
  }

  // member: modetwo
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modetwo: ";
    rosidl_generator_traits::value_to_yaml(msg.modetwo, out);
    out << "\n";
  }

  // member: modethree
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modethree: ";
    rosidl_generator_traits::value_to_yaml(msg.modethree, out);
    out << "\n";
  }

  // member: modefour
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modefour: ";
    rosidl_generator_traits::value_to_yaml(msg.modefour, out);
    out << "\n";
  }

  // member: modefive
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modefive: ";
    rosidl_generator_traits::value_to_yaml(msg.modefive, out);
    out << "\n";
  }

  // member: modesix
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modesix: ";
    rosidl_generator_traits::value_to_yaml(msg.modesix, out);
    out << "\n";
  }

  // member: modeseven
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modeseven: ";
    rosidl_generator_traits::value_to_yaml(msg.modeseven, out);
    out << "\n";
  }

  // member: modeeight
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modeeight: ";
    rosidl_generator_traits::value_to_yaml(msg.modeeight, out);
    out << "\n";
  }

  // member: modenine
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modenine: ";
    rosidl_generator_traits::value_to_yaml(msg.modenine, out);
    out << "\n";
  }

  // member: modeten
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "modeten: ";
    rosidl_generator_traits::value_to_yaml(msg.modeten, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ModeFlag & msg, bool use_flow_style = false)
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
  const px4_msgs::msg::ModeFlag & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4_msgs::msg::ModeFlag & msg)
{
  return px4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4_msgs::msg::ModeFlag>()
{
  return "px4_msgs::msg::ModeFlag";
}

template<>
inline const char * name<px4_msgs::msg::ModeFlag>()
{
  return "px4_msgs/msg/ModeFlag";
}

template<>
struct has_fixed_size<px4_msgs::msg::ModeFlag>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4_msgs::msg::ModeFlag>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4_msgs::msg::ModeFlag>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4_MSGS__MSG__DETAIL__MODE_FLAG__TRAITS_HPP_
