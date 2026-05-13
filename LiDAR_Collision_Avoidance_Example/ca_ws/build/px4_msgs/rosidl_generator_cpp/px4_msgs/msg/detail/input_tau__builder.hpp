// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/InputTau.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__INPUT_TAU__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__INPUT_TAU__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/input_tau__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_InputTau_tau
{
public:
  explicit Init_InputTau_tau(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::InputTau tau(::px4_msgs::msg::InputTau::_tau_type arg)
  {
    msg_.tau = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_input_source
{
public:
  explicit Init_InputTau_input_source(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_tau input_source(::px4_msgs::msg::InputTau::_input_source_type arg)
  {
    msg_.input_source = std::move(arg);
    return Init_InputTau_tau(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_pos
{
public:
  explicit Init_InputTau_pos(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_input_source pos(::px4_msgs::msg::InputTau::_pos_type arg)
  {
    msg_.pos = std::move(arg);
    return Init_InputTau_input_source(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_ye
{
public:
  explicit Init_InputTau_ye(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_pos ye(::px4_msgs::msg::InputTau::_ye_type arg)
  {
    msg_.ye = std::move(arg);
    return Init_InputTau_pos(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_operation_type
{
public:
  explicit Init_InputTau_operation_type(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_ye operation_type(::px4_msgs::msg::InputTau::_operation_type_type arg)
  {
    msg_.operation_type = std::move(arg);
    return Init_InputTau_ye(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_dock_y
{
public:
  explicit Init_InputTau_dock_y(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_operation_type dock_y(::px4_msgs::msg::InputTau::_dock_y_type arg)
  {
    msg_.dock_y = std::move(arg);
    return Init_InputTau_operation_type(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_dock_x
{
public:
  explicit Init_InputTau_dock_x(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_dock_y dock_x(::px4_msgs::msg::InputTau::_dock_x_type arg)
  {
    msg_.dock_x = std::move(arg);
    return Init_InputTau_dock_y(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_docking_guid
{
public:
  explicit Init_InputTau_docking_guid(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_dock_x docking_guid(::px4_msgs::msg::InputTau::_docking_guid_type arg)
  {
    msg_.docking_guid = std::move(arg);
    return Init_InputTau_dock_x(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_wp_guid
{
public:
  explicit Init_InputTau_wp_guid(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_docking_guid wp_guid(::px4_msgs::msg::InputTau::_wp_guid_type arg)
  {
    msg_.wp_guid = std::move(arg);
    return Init_InputTau_docking_guid(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_docking_type
{
public:
  explicit Init_InputTau_docking_type(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_wp_guid docking_type(::px4_msgs::msg::InputTau::_docking_type_type arg)
  {
    msg_.docking_type = std::move(arg);
    return Init_InputTau_wp_guid(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_channel_count
{
public:
  explicit Init_InputTau_channel_count(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_docking_type channel_count(::px4_msgs::msg::InputTau::_channel_count_type arg)
  {
    msg_.channel_count = std::move(arg);
    return Init_InputTau_docking_type(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_timestamp_last_signal
{
public:
  explicit Init_InputTau_timestamp_last_signal(::px4_msgs::msg::InputTau & msg)
  : msg_(msg)
  {}
  Init_InputTau_channel_count timestamp_last_signal(::px4_msgs::msg::InputTau::_timestamp_last_signal_type arg)
  {
    msg_.timestamp_last_signal = std::move(arg);
    return Init_InputTau_channel_count(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

class Init_InputTau_timestamp
{
public:
  Init_InputTau_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InputTau_timestamp_last_signal timestamp(::px4_msgs::msg::InputTau::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_InputTau_timestamp_last_signal(msg_);
  }

private:
  ::px4_msgs::msg::InputTau msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::InputTau>()
{
  return px4_msgs::msg::builder::Init_InputTau_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__INPUT_TAU__BUILDER_HPP_
