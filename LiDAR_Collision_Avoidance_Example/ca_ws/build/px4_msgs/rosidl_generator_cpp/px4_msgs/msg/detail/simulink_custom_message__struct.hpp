// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/SimulinkCustomMessage.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__SimulinkCustomMessage __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__SimulinkCustomMessage __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SimulinkCustomMessage_
{
  using Type = SimulinkCustomMessage_<ContainerAllocator>;

  explicit SimulinkCustomMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->single_a = 0.0f;
      this->single_b = 0.0f;
      this->double_a = 0.0;
      this->double_b = 0.0;
    }
  }

  explicit SimulinkCustomMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->single_a = 0.0f;
      this->single_b = 0.0f;
      this->double_a = 0.0;
      this->double_b = 0.0;
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _single_a_type =
    float;
  _single_a_type single_a;
  using _single_b_type =
    float;
  _single_b_type single_b;
  using _double_a_type =
    double;
  _double_a_type double_a;
  using _double_b_type =
    double;
  _double_b_type double_b;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__single_a(
    const float & _arg)
  {
    this->single_a = _arg;
    return *this;
  }
  Type & set__single_b(
    const float & _arg)
  {
    this->single_b = _arg;
    return *this;
  }
  Type & set__double_a(
    const double & _arg)
  {
    this->double_a = _arg;
    return *this;
  }
  Type & set__double_b(
    const double & _arg)
  {
    this->double_b = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__SimulinkCustomMessage
    std::shared_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__SimulinkCustomMessage
    std::shared_ptr<px4_msgs::msg::SimulinkCustomMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SimulinkCustomMessage_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->single_a != other.single_a) {
      return false;
    }
    if (this->single_b != other.single_b) {
      return false;
    }
    if (this->double_a != other.double_a) {
      return false;
    }
    if (this->double_b != other.double_b) {
      return false;
    }
    return true;
  }
  bool operator!=(const SimulinkCustomMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SimulinkCustomMessage_

// alias to use template instance with default allocator
using SimulinkCustomMessage =
  px4_msgs::msg::SimulinkCustomMessage_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__SIMULINK_CUSTOM_MESSAGE__STRUCT_HPP_
