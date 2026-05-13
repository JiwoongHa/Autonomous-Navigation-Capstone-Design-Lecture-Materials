// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4_msgs:msg/OutputTest.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__BUILDER_HPP_
#define PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4_msgs/msg/detail/output_test__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4_msgs
{

namespace msg
{

namespace builder
{

class Init_OutputTest_nomoto_k
{
public:
  explicit Init_OutputTest_nomoto_k(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  ::px4_msgs::msg::OutputTest nomoto_k(::px4_msgs::msg::OutputTest::_nomoto_k_type arg)
  {
    msg_.nomoto_k = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_nomoto_t
{
public:
  explicit Init_OutputTest_nomoto_t(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  Init_OutputTest_nomoto_k nomoto_t(::px4_msgs::msg::OutputTest::_nomoto_t_type arg)
  {
    msg_.nomoto_t = std::move(arg);
    return Init_OutputTest_nomoto_k(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_eso_type
{
public:
  explicit Init_OutputTest_eso_type(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  Init_OutputTest_nomoto_t eso_type(::px4_msgs::msg::OutputTest::_eso_type_type arg)
  {
    msg_.eso_type = std::move(arg);
    return Init_OutputTest_nomoto_t(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_estimated_d
{
public:
  explicit Init_OutputTest_estimated_d(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  Init_OutputTest_eso_type estimated_d(::px4_msgs::msg::OutputTest::_estimated_d_type arg)
  {
    msg_.estimated_d = std::move(arg);
    return Init_OutputTest_eso_type(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_command
{
public:
  explicit Init_OutputTest_command(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  Init_OutputTest_estimated_d command(::px4_msgs::msg::OutputTest::_command_type arg)
  {
    msg_.command = std::move(arg);
    return Init_OutputTest_estimated_d(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_sates
{
public:
  explicit Init_OutputTest_sates(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  Init_OutputTest_command sates(::px4_msgs::msg::OutputTest::_sates_type arg)
  {
    msg_.sates = std::move(arg);
    return Init_OutputTest_command(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_timestamp_last_signal
{
public:
  explicit Init_OutputTest_timestamp_last_signal(::px4_msgs::msg::OutputTest & msg)
  : msg_(msg)
  {}
  Init_OutputTest_sates timestamp_last_signal(::px4_msgs::msg::OutputTest::_timestamp_last_signal_type arg)
  {
    msg_.timestamp_last_signal = std::move(arg);
    return Init_OutputTest_sates(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

class Init_OutputTest_timestamp
{
public:
  Init_OutputTest_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_OutputTest_timestamp_last_signal timestamp(::px4_msgs::msg::OutputTest::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_OutputTest_timestamp_last_signal(msg_);
  }

private:
  ::px4_msgs::msg::OutputTest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4_msgs::msg::OutputTest>()
{
  return px4_msgs::msg::builder::Init_OutputTest_timestamp();
}

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__BUILDER_HPP_
