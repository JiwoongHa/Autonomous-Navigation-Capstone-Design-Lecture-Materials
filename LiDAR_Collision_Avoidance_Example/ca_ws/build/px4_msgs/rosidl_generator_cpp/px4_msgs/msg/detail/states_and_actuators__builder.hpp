// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/states_and_actuators__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_StatesAndActuators_alpha4_time_log
{
public:
  explicit Init_StatesAndActuators_alpha4_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::StatesAndActuators alpha4_time_log(::px4_msgs::msg::StatesAndActuators::_alpha4_time_log_type arg)
  {
    msg_.alpha4_time_log = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_alpha3_time_log
{
public:
  explicit Init_StatesAndActuators_alpha3_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_alpha4_time_log alpha3_time_log(::px4_msgs::msg::StatesAndActuators::_alpha3_time_log_type arg)
  {
    msg_.alpha3_time_log = std::move(arg);
    return Init_StatesAndActuators_alpha4_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_alpha2_time_log
{
public:
  explicit Init_StatesAndActuators_alpha2_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_alpha3_time_log alpha2_time_log(::px4_msgs::msg::StatesAndActuators::_alpha2_time_log_type arg)
  {
    msg_.alpha2_time_log = std::move(arg);
    return Init_StatesAndActuators_alpha3_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_alpha1_time_log
{
public:
  explicit Init_StatesAndActuators_alpha1_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_alpha2_time_log alpha1_time_log(::px4_msgs::msg::StatesAndActuators::_alpha1_time_log_type arg)
  {
    msg_.alpha1_time_log = std::move(arg);
    return Init_StatesAndActuators_alpha2_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_motor4_time_log
{
public:
  explicit Init_StatesAndActuators_motor4_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_alpha1_time_log motor4_time_log(::px4_msgs::msg::StatesAndActuators::_motor4_time_log_type arg)
  {
    msg_.motor4_time_log = std::move(arg);
    return Init_StatesAndActuators_alpha1_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_motor3_time_log
{
public:
  explicit Init_StatesAndActuators_motor3_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_motor4_time_log motor3_time_log(::px4_msgs::msg::StatesAndActuators::_motor3_time_log_type arg)
  {
    msg_.motor3_time_log = std::move(arg);
    return Init_StatesAndActuators_motor4_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_motor2_time_log
{
public:
  explicit Init_StatesAndActuators_motor2_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_motor3_time_log motor2_time_log(::px4_msgs::msg::StatesAndActuators::_motor2_time_log_type arg)
  {
    msg_.motor2_time_log = std::move(arg);
    return Init_StatesAndActuators_motor3_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_motor1_time_log
{
public:
  explicit Init_StatesAndActuators_motor1_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_motor2_time_log motor1_time_log(::px4_msgs::msg::StatesAndActuators::_motor1_time_log_type arg)
  {
    msg_.motor1_time_log = std::move(arg);
    return Init_StatesAndActuators_motor2_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_taun_time_log
{
public:
  explicit Init_StatesAndActuators_taun_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_motor1_time_log taun_time_log(::px4_msgs::msg::StatesAndActuators::_taun_time_log_type arg)
  {
    msg_.taun_time_log = std::move(arg);
    return Init_StatesAndActuators_motor1_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_tauy_time_log
{
public:
  explicit Init_StatesAndActuators_tauy_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_taun_time_log tauy_time_log(::px4_msgs::msg::StatesAndActuators::_tauy_time_log_type arg)
  {
    msg_.tauy_time_log = std::move(arg);
    return Init_StatesAndActuators_taun_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_taux_time_log
{
public:
  explicit Init_StatesAndActuators_taux_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_tauy_time_log taux_time_log(::px4_msgs::msg::StatesAndActuators::_taux_time_log_type arg)
  {
    msg_.taux_time_log = std::move(arg);
    return Init_StatesAndActuators_tauy_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_psi_time_log
{
public:
  explicit Init_StatesAndActuators_psi_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_taux_time_log psi_time_log(::px4_msgs::msg::StatesAndActuators::_psi_time_log_type arg)
  {
    msg_.psi_time_log = std::move(arg);
    return Init_StatesAndActuators_taux_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_y_time_log
{
public:
  explicit Init_StatesAndActuators_y_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_psi_time_log y_time_log(::px4_msgs::msg::StatesAndActuators::_y_time_log_type arg)
  {
    msg_.y_time_log = std::move(arg);
    return Init_StatesAndActuators_psi_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_x_time_log
{
public:
  explicit Init_StatesAndActuators_x_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_y_time_log x_time_log(::px4_msgs::msg::StatesAndActuators::_x_time_log_type arg)
  {
    msg_.x_time_log = std::move(arg);
    return Init_StatesAndActuators_y_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_r_time_log
{
public:
  explicit Init_StatesAndActuators_r_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_x_time_log r_time_log(::px4_msgs::msg::StatesAndActuators::_r_time_log_type arg)
  {
    msg_.r_time_log = std::move(arg);
    return Init_StatesAndActuators_x_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_v_time_log
{
public:
  explicit Init_StatesAndActuators_v_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_r_time_log v_time_log(::px4_msgs::msg::StatesAndActuators::_v_time_log_type arg)
  {
    msg_.v_time_log = std::move(arg);
    return Init_StatesAndActuators_r_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_u_time_log
{
public:
  explicit Init_StatesAndActuators_u_time_log(::px4_msgs::msg::StatesAndActuators & msg)
  : msg_(msg)
  {}
  Init_StatesAndActuators_v_time_log u_time_log(::px4_msgs::msg::StatesAndActuators::_u_time_log_type arg)
  {
    msg_.u_time_log = std::move(arg);
    return Init_StatesAndActuators_v_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

class Init_StatesAndActuators_timestamp
{
public:
  Init_StatesAndActuators_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StatesAndActuators_u_time_log timestamp(::px4_msgs::msg::StatesAndActuators::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_StatesAndActuators_u_time_log(msg_);
  }

private:
  ::px4_msgs::msg::StatesAndActuators msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::StatesAndActuators>()
{
  return px4_msgs::msg::builder::Init_StatesAndActuators_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__BUILDER_HPP_
