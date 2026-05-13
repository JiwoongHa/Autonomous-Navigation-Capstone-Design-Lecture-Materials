// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__TRAITS_HPP_
#define PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "px4_msgs/msg/detail/states_and_actuators__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace px4_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const StatesAndActuators & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: u_time_log
  {
    out << "u_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.u_time_log, out);
    out << ", ";
  }

  // member: v_time_log
  {
    out << "v_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.v_time_log, out);
    out << ", ";
  }

  // member: r_time_log
  {
    out << "r_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.r_time_log, out);
    out << ", ";
  }

  // member: x_time_log
  {
    out << "x_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.x_time_log, out);
    out << ", ";
  }

  // member: y_time_log
  {
    out << "y_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.y_time_log, out);
    out << ", ";
  }

  // member: psi_time_log
  {
    out << "psi_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.psi_time_log, out);
    out << ", ";
  }

  // member: taux_time_log
  {
    out << "taux_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.taux_time_log, out);
    out << ", ";
  }

  // member: tauy_time_log
  {
    out << "tauy_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.tauy_time_log, out);
    out << ", ";
  }

  // member: taun_time_log
  {
    out << "taun_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.taun_time_log, out);
    out << ", ";
  }

  // member: motor1_time_log
  {
    out << "motor1_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor1_time_log, out);
    out << ", ";
  }

  // member: motor2_time_log
  {
    out << "motor2_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor2_time_log, out);
    out << ", ";
  }

  // member: motor3_time_log
  {
    out << "motor3_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor3_time_log, out);
    out << ", ";
  }

  // member: motor4_time_log
  {
    out << "motor4_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor4_time_log, out);
    out << ", ";
  }

  // member: alpha1_time_log
  {
    out << "alpha1_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha1_time_log, out);
    out << ", ";
  }

  // member: alpha2_time_log
  {
    out << "alpha2_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha2_time_log, out);
    out << ", ";
  }

  // member: alpha3_time_log
  {
    out << "alpha3_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha3_time_log, out);
    out << ", ";
  }

  // member: alpha4_time_log
  {
    out << "alpha4_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha4_time_log, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StatesAndActuators & msg,
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

  // member: u_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "u_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.u_time_log, out);
    out << "\n";
  }

  // member: v_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "v_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.v_time_log, out);
    out << "\n";
  }

  // member: r_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "r_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.r_time_log, out);
    out << "\n";
  }

  // member: x_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.x_time_log, out);
    out << "\n";
  }

  // member: y_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.y_time_log, out);
    out << "\n";
  }

  // member: psi_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "psi_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.psi_time_log, out);
    out << "\n";
  }

  // member: taux_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "taux_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.taux_time_log, out);
    out << "\n";
  }

  // member: tauy_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tauy_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.tauy_time_log, out);
    out << "\n";
  }

  // member: taun_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "taun_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.taun_time_log, out);
    out << "\n";
  }

  // member: motor1_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor1_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor1_time_log, out);
    out << "\n";
  }

  // member: motor2_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor2_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor2_time_log, out);
    out << "\n";
  }

  // member: motor3_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor3_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor3_time_log, out);
    out << "\n";
  }

  // member: motor4_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "motor4_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.motor4_time_log, out);
    out << "\n";
  }

  // member: alpha1_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alpha1_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha1_time_log, out);
    out << "\n";
  }

  // member: alpha2_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alpha2_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha2_time_log, out);
    out << "\n";
  }

  // member: alpha3_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alpha3_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha3_time_log, out);
    out << "\n";
  }

  // member: alpha4_time_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alpha4_time_log: ";
    rosidl_generator_traits::value_to_yaml(msg.alpha4_time_log, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StatesAndActuators & msg, bool use_flow_style = false)
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
  const px4_msgs::msg::StatesAndActuators & msg,
  std::ostream & out, size_t indentation = 0)
{
  px4_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use px4_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const px4_msgs::msg::StatesAndActuators & msg)
{
  return px4_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<px4_msgs::msg::StatesAndActuators>()
{
  return "px4_msgs::msg::StatesAndActuators";
}

template<>
inline const char * name<px4_msgs::msg::StatesAndActuators>()
{
  return "px4_msgs/msg/StatesAndActuators";
}

template<>
struct has_fixed_size<px4_msgs::msg::StatesAndActuators>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<px4_msgs::msg::StatesAndActuators>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<px4_msgs::msg::StatesAndActuators>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__TRAITS_HPP_
