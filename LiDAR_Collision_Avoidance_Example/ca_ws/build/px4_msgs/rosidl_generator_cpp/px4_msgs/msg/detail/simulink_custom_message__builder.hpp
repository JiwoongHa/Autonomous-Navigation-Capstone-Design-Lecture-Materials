// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/SimulinkCustomMessage.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/simulink_custom_message__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_SimulinkCustomMessage_double_b
{
public:
  explicit Init_SimulinkCustomMessage_double_b(::px4_msgs::msg::SimulinkCustomMessage & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::SimulinkCustomMessage double_b(::px4_msgs::msg::SimulinkCustomMessage::_double_b_type arg)
  {
    msg_.double_b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::SimulinkCustomMessage msg_;
};

class Init_SimulinkCustomMessage_double_a
{
public:
  explicit Init_SimulinkCustomMessage_double_a(::px4_msgs::msg::SimulinkCustomMessage & msg)
  : msg_(msg)
  {}
  Init_SimulinkCustomMessage_double_b double_a(::px4_msgs::msg::SimulinkCustomMessage::_double_a_type arg)
  {
    msg_.double_a = std::move(arg);
    return Init_SimulinkCustomMessage_double_b(msg_);
  }

private:
  ::px4_msgs::msg::SimulinkCustomMessage msg_;
};

class Init_SimulinkCustomMessage_single_b
{
public:
  explicit Init_SimulinkCustomMessage_single_b(::px4_msgs::msg::SimulinkCustomMessage & msg)
  : msg_(msg)
  {}
  Init_SimulinkCustomMessage_double_a single_b(::px4_msgs::msg::SimulinkCustomMessage::_single_b_type arg)
  {
    msg_.single_b = std::move(arg);
    return Init_SimulinkCustomMessage_double_a(msg_);
  }

private:
  ::px4_msgs::msg::SimulinkCustomMessage msg_;
};

class Init_SimulinkCustomMessage_single_a
{
public:
  explicit Init_SimulinkCustomMessage_single_a(::px4_msgs::msg::SimulinkCustomMessage & msg)
  : msg_(msg)
  {}
  Init_SimulinkCustomMessage_single_b single_a(::px4_msgs::msg::SimulinkCustomMessage::_single_a_type arg)
  {
    msg_.single_a = std::move(arg);
    return Init_SimulinkCustomMessage_single_b(msg_);
  }

private:
  ::px4_msgs::msg::SimulinkCustomMessage msg_;
};

class Init_SimulinkCustomMessage_timestamp
{
public:
  Init_SimulinkCustomMessage_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SimulinkCustomMessage_single_a timestamp(::px4_msgs::msg::SimulinkCustomMessage::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_SimulinkCustomMessage_single_a(msg_);
  }

private:
  ::px4_msgs::msg::SimulinkCustomMessage msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::SimulinkCustomMessage>()
{
  return px4_msgs::msg::builder::Init_SimulinkCustomMessage_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__BUILDER_HPP_
