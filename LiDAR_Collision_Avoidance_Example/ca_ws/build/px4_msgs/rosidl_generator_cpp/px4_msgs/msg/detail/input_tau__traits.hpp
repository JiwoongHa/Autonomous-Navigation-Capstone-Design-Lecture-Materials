// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4_msgs:msg/InputTau.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__INPUT_TAU__TRAITS_HPP_
#define PX4_MSGS__MSG__DETAIL__INPUT_TAU__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4_msgs/msg/detail/input_tau__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const InputTau & msg,
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

  // member: channel_count
  {
    out << "channel_count: ";
    rosidl_generator_traits::value_to_yaml(msg.channel_count, out);
    out << ", ";
  }

  // member: docking_type
  {
    out << "docking_type: ";
    rosidl_generator_traits::value_to_yaml(msg.docking_type, out);
    out << ", ";
  }

  // member: wp_guid
  {
    out << "wp_guid: ";
    rosidl_generator_traits::value_to_yaml(msg.wp_guid, out);
    out << ", ";
  }

  // member: docking_guid
  {
    out << "docking_guid: ";
    rosidl_generator_traits::value_to_yaml(msg.docking_guid, out);
    out << ", ";
  }

  // member: dock_x
  {
    if (msg.dock_x.size() == 0) {
      out << "dock_x: []";
    } else {
      out << "dock_x: [";
      size_t pending_items = msg.dock_x.size();
      for (auto item : msg.dock_x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: dock_y
  {
    if (msg.dock_y.size() == 0) {
      out << "dock_y: []";
    } else {
      out << "dock_y: [";
      size_t pending_items = msg.dock_y.size();
      for (auto item : msg.dock_y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: operation_type
  {
    out << "operation_type: ";
    rosidl_generator_traits::value_to_yaml(msg.operation_type, out);
    out << ", ";
  }

  // member: ye
  {
    out << "ye: ";
    rosidl_generator_traits::value_to_yaml(msg.ye, out);
    out << ", ";
  }

  // member: pos
  {
    if (msg.pos.size() == 0) {
      out << "pos: []";
    } else {
      out << "pos: [";
      size_t pending_items = msg.pos.size();
      for (auto item : msg.pos) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: input_source
  {
    out << "input_source: ";
    rosidl_generator_traits::value_to_yaml(msg.input_source, out);
    out << ", ";
  }

  // member: tau
  {
    if (msg.tau.size() == 0) {
      out << "tau: []";
    } else {
      out << "tau: [";
      size_t pending_items = msg.tau.size();
      for (auto item : msg.tau) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const InputTau & msg,
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

  // member: channel_count
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "channel_count: ";
    rosidl_generator_traits::value_to_yaml(msg.channel_count, out);
    out << "\n";
  }

  // member: docking_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "docking_type: ";
    rosidl_generator_traits::value_to_yaml(msg.docking_type, out);
    out << "\n";
  }

  // member: wp_guid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wp_guid: ";
    rosidl_generator_traits::value_to_yaml(msg.wp_guid, out);
    out << "\n";
  }

  // member: docking_guid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "docking_guid: ";
    rosidl_generator_traits::value_to_yaml(msg.docking_guid, out);
    out << "\n";
  }

  // member: dock_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.dock_x.size() == 0) {
      out << "dock_x: []\n";
    } else {
      out << "dock_x:\n";
      for (auto item : msg.dock_x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: dock_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.dock_y.size() == 0) {
      out << "dock_y: []\n";
    } else {
      out << "dock_y:\n";
      for (auto item : msg.dock_y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: operation_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "operation_type: ";
    rosidl_generator_traits::value_to_yaml(msg.operation_type, out);
    out << "\n";
  }

  // member: ye
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ye: ";
    rosidl_generator_traits::value_to_yaml(msg.ye, out);
    out << "\n";
  }

  // member: pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pos.size() == 0) {
      out << "pos: []\n";
    } else {
      out << "pos:\n";
      for (auto item : msg.pos) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: input_source
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "input_source: ";
    rosidl_generator_traits::value_to_yaml(msg.input_source, out);
    out << "\n";
  }

  // member: tau
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.tau.size() == 0) {
      out << "tau: []\n";
    } else {
      out << "tau:\n";
      for (auto item : msg.tau) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const InputTau & msg, bool use_flow_style = false)
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
  const px4_msgs::msg::InputTau & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4_msgs::msg::InputTau & msg)
{
  return px4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4_msgs::msg::InputTau>()
{
  return "px4_msgs::msg::InputTau";
}

template<>
inline const char * name<px4_msgs::msg::InputTau>()
{
  return "px4_msgs/msg/InputTau";
}

template<>
struct has_fixed_size<px4_msgs::msg::InputTau>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4_msgs::msg::InputTau>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4_msgs::msg::InputTau>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4_MSGS__MSG__DETAIL__INPUT_TAU__TRAITS_HPP_
