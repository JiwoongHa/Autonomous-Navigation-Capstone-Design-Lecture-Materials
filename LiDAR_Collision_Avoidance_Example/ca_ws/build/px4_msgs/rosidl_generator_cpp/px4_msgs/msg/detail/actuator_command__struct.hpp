// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/ActuatorCommand.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__ActuatorCommand __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__ActuatorCommand __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ActuatorCommand_
{
  using Type = ActuatorCommand_<ContainerAllocator>;

  explicit ActuatorCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->motor_pwm = 0.0;
      this->steering_pwm = 0.0;
    }
  }

  explicit ActuatorCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->motor_pwm = 0.0;
      this->steering_pwm = 0.0;
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _motor_pwm_type =
    double;
  _motor_pwm_type motor_pwm;
  using _steering_pwm_type =
    double;
  _steering_pwm_type steering_pwm;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__motor_pwm(
    const double & _arg)
  {
    this->motor_pwm = _arg;
    return *this;
  }
  Type & set__steering_pwm(
    const double & _arg)
  {
    this->steering_pwm = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::ActuatorCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::ActuatorCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::ActuatorCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::ActuatorCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__ActuatorCommand
    std::shared_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__ActuatorCommand
    std::shared_ptr<px4_msgs::msg::ActuatorCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ActuatorCommand_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->motor_pwm != other.motor_pwm) {
      return false;
    }
    if (this->steering_pwm != other.steering_pwm) {
      return false;
    }
    return true;
  }
  bool operator!=(const ActuatorCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ActuatorCommand_

// alias to use template instance with default allocator
using ActuatorCommand =
  px4_msgs::msg::ActuatorCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__ACTUATOR_COMMAND__STRUCT_HPP_
