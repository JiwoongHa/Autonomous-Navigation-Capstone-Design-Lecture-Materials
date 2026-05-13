// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4_msgs:msg/OutputTest.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__TRAITS_HPP_
#define PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4_msgs/msg/detail/output_test__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const OutputTest & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: timestamp_last_signal
  {
    out << "timestamp_last_signal: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp_last_signal, out);
    out << ", ";
  }

  // member: sates
  {
    if (msg.sates.size() == 0) {
      out << "sates: []";
    } else {
      out << "sates: [";
      size_t pending_items = msg.sates.size();
      for (auto item : msg.sates) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: command
  {
    if (msg.command.size() == 0) {
      out << "command: []";
    } else {
      out << "command: [";
      size_t pending_items = msg.command.size();
      for (auto item : msg.command) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: estimated_d
  {
    out << "estimated_d: ";
    rosidl_generator_traits::value_to_yaml(msg.estimated_d, out);
    out << ", ";
  }

  // member: eso_type
  {
    out << "eso_type: ";
    rosidl_generator_traits::value_to_yaml(msg.eso_type, out);
    out << ", ";
  }

  // member: nomoto_t
  {
    out << "nomoto_t: ";
    rosidl_generator_traits::value_to_yaml(msg.nomoto_t, out);
    out << ", ";
  }

  // member: nomoto_k
  {
    out << "nomoto_k: ";
    rosidl_generator_traits::value_to_yaml(msg.nomoto_k, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OutputTest & msg,
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

  // member: timestamp_last_signal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp_last_signal: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp_last_signal, out);
    out << "\n";
  }

  // member: sates
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.sates.size() == 0) {
      out << "sates: []\n";
    } else {
      out << "sates:\n";
      for (auto item : msg.sates) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.command.size() == 0) {
      out << "command: []\n";
    } else {
      out << "command:\n";
      for (auto item : msg.command) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: estimated_d
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "estimated_d: ";
    rosidl_generator_traits::value_to_yaml(msg.estimated_d, out);
    out << "\n";
  }

  // member: eso_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "eso_type: ";
    rosidl_generator_traits::value_to_yaml(msg.eso_type, out);
    out << "\n";
  }

  // member: nomoto_t
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "nomoto_t: ";
    rosidl_generator_traits::value_to_yaml(msg.nomoto_t, out);
    out << "\n";
  }

  // member: nomoto_k
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "nomoto_k: ";
    rosidl_generator_traits::value_to_yaml(msg.nomoto_k, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OutputTest & msg, bool use_flow_style = false)
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
  const px4_msgs::msg::OutputTest & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4_msgs::msg::OutputTest & msg)
{
  return px4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4_msgs::msg::OutputTest>()
{
  return "px4_msgs::msg::OutputTest";
}

template<>
inline const char * name<px4_msgs::msg::OutputTest>()
{
  return "px4_msgs/msg/OutputTest";
}

template<>
struct has_fixed_size<px4_msgs::msg::OutputTest>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4_msgs::msg::OutputTest>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4_msgs::msg::OutputTest>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__TRAITS_HPP_
