// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/ModeFlag.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__MODE_FLAG__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__MODE_FLAG__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/mode_flag__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_ModeFlag_modeten
{
public:
  explicit Init_ModeFlag_modeten(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::ModeFlag modeten(::px4_msgs::msg::ModeFlag::_modeten_type arg)
  {
    msg_.modeten = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modenine
{
public:
  explicit Init_ModeFlag_modenine(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modeten modenine(::px4_msgs::msg::ModeFlag::_modenine_type arg)
  {
    msg_.modenine = std::move(arg);
    return Init_ModeFlag_modeten(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modeeight
{
public:
  explicit Init_ModeFlag_modeeight(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modenine modeeight(::px4_msgs::msg::ModeFlag::_modeeight_type arg)
  {
    msg_.modeeight = std::move(arg);
    return Init_ModeFlag_modenine(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modeseven
{
public:
  explicit Init_ModeFlag_modeseven(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modeeight modeseven(::px4_msgs::msg::ModeFlag::_modeseven_type arg)
  {
    msg_.modeseven = std::move(arg);
    return Init_ModeFlag_modeeight(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modesix
{
public:
  explicit Init_ModeFlag_modesix(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modeseven modesix(::px4_msgs::msg::ModeFlag::_modesix_type arg)
  {
    msg_.modesix = std::move(arg);
    return Init_ModeFlag_modeseven(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modefive
{
public:
  explicit Init_ModeFlag_modefive(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modesix modefive(::px4_msgs::msg::ModeFlag::_modefive_type arg)
  {
    msg_.modefive = std::move(arg);
    return Init_ModeFlag_modesix(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modefour
{
public:
  explicit Init_ModeFlag_modefour(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modefive modefour(::px4_msgs::msg::ModeFlag::_modefour_type arg)
  {
    msg_.modefour = std::move(arg);
    return Init_ModeFlag_modefive(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modethree
{
public:
  explicit Init_ModeFlag_modethree(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modefour modethree(::px4_msgs::msg::ModeFlag::_modethree_type arg)
  {
    msg_.modethree = std::move(arg);
    return Init_ModeFlag_modefour(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modetwo
{
public:
  explicit Init_ModeFlag_modetwo(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modethree modetwo(::px4_msgs::msg::ModeFlag::_modetwo_type arg)
  {
    msg_.modetwo = std::move(arg);
    return Init_ModeFlag_modethree(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_modeone
{
public:
  explicit Init_ModeFlag_modeone(::px4_msgs::msg::ModeFlag & msg)
  : msg_(msg)
  {}
  Init_ModeFlag_modetwo modeone(::px4_msgs::msg::ModeFlag::_modeone_type arg)
  {
    msg_.modeone = std::move(arg);
    return Init_ModeFlag_modetwo(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

class Init_ModeFlag_timestamp
{
public:
  Init_ModeFlag_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ModeFlag_modeone timestamp(::px4_msgs::msg::ModeFlag::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_ModeFlag_modeone(msg_);
  }

private:
  ::px4_msgs::msg::ModeFlag msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::ModeFlag>()
{
  return px4_msgs::msg::builder::Init_ModeFlag_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__MODE_FLAG__BUILDER_HPP_
