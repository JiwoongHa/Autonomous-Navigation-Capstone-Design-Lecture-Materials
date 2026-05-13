// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/OutputTest.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__OutputTest __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__OutputTest __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct OutputTest_
{
  using Type = OutputTest_<ContainerAllocator>;

  explicit OutputTest_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->timestamp_last_signal = 0ull;
      std::fill<typename std::array<double, 9>::iterator, double>(this->sates.begin(), this->sates.end(), 0.0);
      std::fill<typename std::array<double, 7>::iterator, double>(this->command.begin(), this->command.end(), 0.0);
      this->estimated_d = 0.0;
      this->eso_type = 0;
      this->nomoto_t = 0.0f;
      this->nomoto_k = 0.0f;
    }
  }

  explicit OutputTest_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : sates(_alloc),
    command(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->timestamp_last_signal = 0ull;
      std::fill<typename std::array<double, 9>::iterator, double>(this->sates.begin(), this->sates.end(), 0.0);
      std::fill<typename std::array<double, 7>::iterator, double>(this->command.begin(), this->command.end(), 0.0);
      this->estimated_d = 0.0;
      this->eso_type = 0;
      this->nomoto_t = 0.0f;
      this->nomoto_k = 0.0f;
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _timestamp_last_signal_type =
    uint64_t;
  _timestamp_last_signal_type timestamp_last_signal;
  using _sates_type =
    std::array<double, 9>;
  _sates_type sates;
  using _command_type =
    std::array<double, 7>;
  _command_type command;
  using _estimated_d_type =
    double;
  _estimated_d_type estimated_d;
  using _eso_type_type =
    int8_t;
  _eso_type_type eso_type;
  using _nomoto_t_type =
    float;
  _nomoto_t_type nomoto_t;
  using _nomoto_k_type =
    float;
  _nomoto_k_type nomoto_k;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__timestamp_last_signal(
    const uint64_t & _arg)
  {
    this->timestamp_last_signal = _arg;
    return *this;
  }
  Type & set__sates(
    const std::array<double, 9> & _arg)
  {
    this->sates = _arg;
    return *this;
  }
  Type & set__command(
    const std::array<double, 7> & _arg)
  {
    this->command = _arg;
    return *this;
  }
  Type & set__estimated_d(
    const double & _arg)
  {
    this->estimated_d = _arg;
    return *this;
  }
  Type & set__eso_type(
    const int8_t & _arg)
  {
    this->eso_type = _arg;
    return *this;
  }
  Type & set__nomoto_t(
    const float & _arg)
  {
    this->nomoto_t = _arg;
    return *this;
  }
  Type & set__nomoto_k(
    const float & _arg)
  {
    this->nomoto_k = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::OutputTest_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::OutputTest_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::OutputTest_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::OutputTest_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__OutputTest
    std::shared_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__OutputTest
    std::shared_ptr<px4_msgs::msg::OutputTest_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const OutputTest_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->timestamp_last_signal != other.timestamp_last_signal) {
      return false;
    }
    if (this->sates != other.sates) {
      return false;
    }
    if (this->command != other.command) {
      return false;
    }
    if (this->estimated_d != other.estimated_d) {
      return false;
    }
    if (this->eso_type != other.eso_type) {
      return false;
    }
    if (this->nomoto_t != other.nomoto_t) {
      return false;
    }
    if (this->nomoto_k != other.nomoto_k) {
      return false;
    }
    return true;
  }
  bool operator!=(const OutputTest_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct OutputTest_

// alias to use template instance with default allocator
using OutputTest =
  px4_msgs::msg::OutputTest_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__OUTPUT_TEST__STRUCT_HPP_
