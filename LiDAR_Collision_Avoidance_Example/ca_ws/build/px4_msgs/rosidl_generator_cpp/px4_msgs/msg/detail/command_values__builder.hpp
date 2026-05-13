// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/command_values__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_CommandValues_y_berth_end
{
public:
  explicit Init_CommandValues_y_berth_end(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::CommandValues y_berth_end(::px4_msgs::msg::CommandValues::_y_berth_end_type arg)
  {
    msg_.y_berth_end = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_x_berth_end
{
public:
  explicit Init_CommandValues_x_berth_end(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_y_berth_end x_berth_end(::px4_msgs::msg::CommandValues::_x_berth_end_type arg)
  {
    msg_.x_berth_end = std::move(arg);
    return Init_CommandValues_y_berth_end(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_y_berth_start
{
public:
  explicit Init_CommandValues_y_berth_start(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_x_berth_end y_berth_start(::px4_msgs::msg::CommandValues::_y_berth_start_type arg)
  {
    msg_.y_berth_start = std::move(arg);
    return Init_CommandValues_x_berth_end(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_x_berth_start
{
public:
  explicit Init_CommandValues_x_berth_start(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_y_berth_start x_berth_start(::px4_msgs::msg::CommandValues::_x_berth_start_type arg)
  {
    msg_.x_berth_start = std::move(arg);
    return Init_CommandValues_y_berth_start(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_ye_log
{
public:
  explicit Init_CommandValues_ye_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_x_berth_start ye_log(::px4_msgs::msg::CommandValues::_ye_log_type arg)
  {
    msg_.ye_log = std::move(arg);
    return Init_CommandValues_x_berth_start(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_psi_cmd_log
{
public:
  explicit Init_CommandValues_psi_cmd_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_ye_log psi_cmd_log(::px4_msgs::msg::CommandValues::_psi_cmd_log_type arg)
  {
    msg_.psi_cmd_log = std::move(arg);
    return Init_CommandValues_ye_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_y_cmd_log
{
public:
  explicit Init_CommandValues_y_cmd_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_psi_cmd_log y_cmd_log(::px4_msgs::msg::CommandValues::_y_cmd_log_type arg)
  {
    msg_.y_cmd_log = std::move(arg);
    return Init_CommandValues_psi_cmd_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_x_cmd_log
{
public:
  explicit Init_CommandValues_x_cmd_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_y_cmd_log x_cmd_log(::px4_msgs::msg::CommandValues::_x_cmd_log_type arg)
  {
    msg_.x_cmd_log = std::move(arg);
    return Init_CommandValues_y_cmd_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_u_cmd_log
{
public:
  explicit Init_CommandValues_u_cmd_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_x_cmd_log u_cmd_log(::px4_msgs::msg::CommandValues::_u_cmd_log_type arg)
  {
    msg_.u_cmd_log = std::move(arg);
    return Init_CommandValues_x_cmd_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_wp_mode_log
{
public:
  explicit Init_CommandValues_wp_mode_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_u_cmd_log wp_mode_log(::px4_msgs::msg::CommandValues::_wp_mode_log_type arg)
  {
    msg_.wp_mode_log = std::move(arg);
    return Init_CommandValues_u_cmd_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_d_mode_log
{
public:
  explicit Init_CommandValues_d_mode_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_wp_mode_log d_mode_log(::px4_msgs::msg::CommandValues::_d_mode_log_type arg)
  {
    msg_.d_mode_log = std::move(arg);
    return Init_CommandValues_wp_mode_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_rc_on_off_log
{
public:
  explicit Init_CommandValues_rc_on_off_log(::px4_msgs::msg::CommandValues & msg)
  : msg_(msg)
  {}
  Init_CommandValues_d_mode_log rc_on_off_log(::px4_msgs::msg::CommandValues::_rc_on_off_log_type arg)
  {
    msg_.rc_on_off_log = std::move(arg);
    return Init_CommandValues_d_mode_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

class Init_CommandValues_timestamp
{
public:
  Init_CommandValues_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CommandValues_rc_on_off_log timestamp(::px4_msgs::msg::CommandValues::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_CommandValues_rc_on_off_log(msg_);
  }

private:
  ::px4_msgs::msg::CommandValues msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::CommandValues>()
{
  return px4_msgs::msg::builder::Init_CommandValues_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__BUILDER_HPP_
