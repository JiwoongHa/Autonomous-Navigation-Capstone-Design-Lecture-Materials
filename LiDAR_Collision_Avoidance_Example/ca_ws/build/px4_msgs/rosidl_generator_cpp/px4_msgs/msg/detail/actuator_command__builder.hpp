// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/ActuatorCommand.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/actuator_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_ActuatorCommand_steering_pwm
{
public:
  explicit Init_ActuatorCommand_steering_pwm(::px4_msgs::msg::ActuatorCommand & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::ActuatorCommand steering_pwm(::px4_msgs::msg::ActuatorCommand::_steering_pwm_type arg)
  {
    msg_.steering_pwm = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::ActuatorCommand msg_;
};

class Init_ActuatorCommand_motor_pwm
{
public:
  explicit Init_ActuatorCommand_motor_pwm(::px4_msgs::msg::ActuatorCommand & msg)
  : msg_(msg)
  {}
  Init_ActuatorCommand_steering_pwm motor_pwm(::px4_msgs::msg::ActuatorCommand::_motor_pwm_type arg)
  {
    msg_.motor_pwm = std::move(arg);
    return Init_ActuatorCommand_steering_pwm(msg_);
  }

private:
  ::px4_msgs::msg::ActuatorCommand msg_;
};

class Init_ActuatorCommand_timestamp
{
public:
  Init_ActuatorCommand_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ActuatorCommand_motor_pwm timestamp(::px4_msgs::msg::ActuatorCommand::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_ActuatorCommand_motor_pwm(msg_);
  }

private:
  ::px4_msgs::msg::ActuatorCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::ActuatorCommand>()
{
  return px4_msgs::msg::builder::Init_ActuatorCommand_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__BUILDER_HPP_
