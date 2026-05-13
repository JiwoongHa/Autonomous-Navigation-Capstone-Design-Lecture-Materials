// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__CommandValues __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__CommandValues __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CommandValues_
{
  using Type = CommandValues_<ContainerAllocator>;

  explicit CommandValues_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->rc_on_off_log = 0.0f;
      this->d_mode_log = 0.0f;
      this->wp_mode_log = 0.0f;
      this->u_cmd_log = 0.0;
      this->x_cmd_log = 0.0;
      this->y_cmd_log = 0.0;
      this->psi_cmd_log = 0.0;
      this->ye_log = 0.0;
      this->x_berth_start = 0.0;
      this->y_berth_start = 0.0;
      this->x_berth_end = 0.0;
      this->y_berth_end = 0.0;
    }
  }

  explicit CommandValues_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->rc_on_off_log = 0.0f;
      this->d_mode_log = 0.0f;
      this->wp_mode_log = 0.0f;
      this->u_cmd_log = 0.0;
      this->x_cmd_log = 0.0;
      this->y_cmd_log = 0.0;
      this->psi_cmd_log = 0.0;
      this->ye_log = 0.0;
      this->x_berth_start = 0.0;
      this->y_berth_start = 0.0;
      this->x_berth_end = 0.0;
      this->y_berth_end = 0.0;
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _rc_on_off_log_type =
    float;
  _rc_on_off_log_type rc_on_off_log;
  using _d_mode_log_type =
    float;
  _d_mode_log_type d_mode_log;
  using _wp_mode_log_type =
    float;
  _wp_mode_log_type wp_mode_log;
  using _u_cmd_log_type =
    double;
  _u_cmd_log_type u_cmd_log;
  using _x_cmd_log_type =
    double;
  _x_cmd_log_type x_cmd_log;
  using _y_cmd_log_type =
    double;
  _y_cmd_log_type y_cmd_log;
  using _psi_cmd_log_type =
    double;
  _psi_cmd_log_type psi_cmd_log;
  using _ye_log_type =
    double;
  _ye_log_type ye_log;
  using _x_berth_start_type =
    double;
  _x_berth_start_type x_berth_start;
  using _y_berth_start_type =
    double;
  _y_berth_start_type y_berth_start;
  using _x_berth_end_type =
    double;
  _x_berth_end_type x_berth_end;
  using _y_berth_end_type =
    double;
  _y_berth_end_type y_berth_end;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__rc_on_off_log(
    const float & _arg)
  {
    this->rc_on_off_log = _arg;
    return *this;
  }
  Type & set__d_mode_log(
    const float & _arg)
  {
    this->d_mode_log = _arg;
    return *this;
  }
  Type & set__wp_mode_log(
    const float & _arg)
  {
    this->wp_mode_log = _arg;
    return *this;
  }
  Type & set__u_cmd_log(
    const double & _arg)
  {
    this->u_cmd_log = _arg;
    return *this;
  }
  Type & set__x_cmd_log(
    const double & _arg)
  {
    this->x_cmd_log = _arg;
    return *this;
  }
  Type & set__y_cmd_log(
    const double & _arg)
  {
    this->y_cmd_log = _arg;
    return *this;
  }
  Type & set__psi_cmd_log(
    const double & _arg)
  {
    this->psi_cmd_log = _arg;
    return *this;
  }
  Type & set__ye_log(
    const double & _arg)
  {
    this->ye_log = _arg;
    return *this;
  }
  Type & set__x_berth_start(
    const double & _arg)
  {
    this->x_berth_start = _arg;
    return *this;
  }
  Type & set__y_berth_start(
    const double & _arg)
  {
    this->y_berth_start = _arg;
    return *this;
  }
  Type & set__x_berth_end(
    const double & _arg)
  {
    this->x_berth_end = _arg;
    return *this;
  }
  Type & set__y_berth_end(
    const double & _arg)
  {
    this->y_berth_end = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::CommandValues_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::CommandValues_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::CommandValues_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::CommandValues_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__CommandValues
    std::shared_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__CommandValues
    std::shared_ptr<px4_msgs::msg::CommandValues_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CommandValues_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->rc_on_off_log != other.rc_on_off_log) {
      return false;
    }
    if (this->d_mode_log != other.d_mode_log) {
      return false;
    }
    if (this->wp_mode_log != other.wp_mode_log) {
      return false;
    }
    if (this->u_cmd_log != other.u_cmd_log) {
      return false;
    }
    if (this->x_cmd_log != other.x_cmd_log) {
      return false;
    }
    if (this->y_cmd_log != other.y_cmd_log) {
      return false;
    }
    if (this->psi_cmd_log != other.psi_cmd_log) {
      return false;
    }
    if (this->ye_log != other.ye_log) {
      return false;
    }
    if (this->x_berth_start != other.x_berth_start) {
      return false;
    }
    if (this->y_berth_start != other.y_berth_start) {
      return false;
    }
    if (this->x_berth_end != other.x_berth_end) {
      return false;
    }
    if (this->y_berth_end != other.y_berth_end) {
      return false;
    }
    return true;
  }
  bool operator!=(const CommandValues_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CommandValues_

// alias to use template instance with default allocator
using CommandValues =
  px4_msgs::msg::CommandValues_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__COMMAND_VALUES__STRUCT_HPP_
