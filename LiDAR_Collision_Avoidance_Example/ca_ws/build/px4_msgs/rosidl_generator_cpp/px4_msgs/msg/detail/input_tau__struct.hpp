// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/InputTau.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__INPUT_TAU__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__INPUT_TAU__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__InputTau __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__InputTau __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct InputTau_
{
  using Type = InputTau_<ContainerAllocator>;

  explicit InputTau_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->timestamp_last_signal = 0ull;
      this->channel_count = 0;
      this->docking_type = 0;
      this->wp_guid = 0;
      this->docking_guid = 0;
      std::fill<typename std::array<double, 2>::iterator, double>(this->dock_x.begin(), this->dock_x.end(), 0.0);
      std::fill<typename std::array<double, 2>::iterator, double>(this->dock_y.begin(), this->dock_y.end(), 0.0);
      this->operation_type = 0;
      this->ye = 0.0;
      std::fill<typename std::array<double, 3>::iterator, double>(this->pos.begin(), this->pos.end(), 0.0);
      this->input_source = 0;
      std::fill<typename std::array<double, 3>::iterator, double>(this->tau.begin(), this->tau.end(), 0.0);
    }
  }

  explicit InputTau_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : dock_x(_alloc),
    dock_y(_alloc),
    pos(_alloc),
    tau(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->timestamp_last_signal = 0ull;
      this->channel_count = 0;
      this->docking_type = 0;
      this->wp_guid = 0;
      this->docking_guid = 0;
      std::fill<typename std::array<double, 2>::iterator, double>(this->dock_x.begin(), this->dock_x.end(), 0.0);
      std::fill<typename std::array<double, 2>::iterator, double>(this->dock_y.begin(), this->dock_y.end(), 0.0);
      this->operation_type = 0;
      this->ye = 0.0;
      std::fill<typename std::array<double, 3>::iterator, double>(this->pos.begin(), this->pos.end(), 0.0);
      this->input_source = 0;
      std::fill<typename std::array<double, 3>::iterator, double>(this->tau.begin(), this->tau.end(), 0.0);
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _timestamp_last_signal_type =
    uint64_t;
  _timestamp_last_signal_type timestamp_last_signal;
  using _channel_count_type =
    uint8_t;
  _channel_count_type channel_count;
  using _docking_type_type =
    int8_t;
  _docking_type_type docking_type;
  using _wp_guid_type =
    int8_t;
  _wp_guid_type wp_guid;
  using _docking_guid_type =
    int8_t;
  _docking_guid_type docking_guid;
  using _dock_x_type =
    std::array<double, 2>;
  _dock_x_type dock_x;
  using _dock_y_type =
    std::array<double, 2>;
  _dock_y_type dock_y;
  using _operation_type_type =
    int8_t;
  _operation_type_type operation_type;
  using _ye_type =
    double;
  _ye_type ye;
  using _pos_type =
    std::array<double, 3>;
  _pos_type pos;
  using _input_source_type =
    uint8_t;
  _input_source_type input_source;
  using _tau_type =
    std::array<double, 3>;
  _tau_type tau;

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
  Type & set__channel_count(
    const uint8_t & _arg)
  {
    this->channel_count = _arg;
    return *this;
  }
  Type & set__docking_type(
    const int8_t & _arg)
  {
    this->docking_type = _arg;
    return *this;
  }
  Type & set__wp_guid(
    const int8_t & _arg)
  {
    this->wp_guid = _arg;
    return *this;
  }
  Type & set__docking_guid(
    const int8_t & _arg)
  {
    this->docking_guid = _arg;
    return *this;
  }
  Type & set__dock_x(
    const std::array<double, 2> & _arg)
  {
    this->dock_x = _arg;
    return *this;
  }
  Type & set__dock_y(
    const std::array<double, 2> & _arg)
  {
    this->dock_y = _arg;
    return *this;
  }
  Type & set__operation_type(
    const int8_t & _arg)
  {
    this->operation_type = _arg;
    return *this;
  }
  Type & set__ye(
    const double & _arg)
  {
    this->ye = _arg;
    return *this;
  }
  Type & set__pos(
    const std::array<double, 3> & _arg)
  {
    this->pos = _arg;
    return *this;
  }
  Type & set__input_source(
    const uint8_t & _arg)
  {
    this->input_source = _arg;
    return *this;
  }
  Type & set__tau(
    const std::array<double, 3> & _arg)
  {
    this->tau = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::InputTau_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::InputTau_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::InputTau_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::InputTau_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::InputTau_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::InputTau_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::InputTau_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::InputTau_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::InputTau_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::InputTau_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__InputTau
    std::shared_ptr<px4_msgs::msg::InputTau_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__InputTau
    std::shared_ptr<px4_msgs::msg::InputTau_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const InputTau_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->timestamp_last_signal != other.timestamp_last_signal) {
      return false;
    }
    if (this->channel_count != other.channel_count) {
      return false;
    }
    if (this->docking_type != other.docking_type) {
      return false;
    }
    if (this->wp_guid != other.wp_guid) {
      return false;
    }
    if (this->docking_guid != other.docking_guid) {
      return false;
    }
    if (this->dock_x != other.dock_x) {
      return false;
    }
    if (this->dock_y != other.dock_y) {
      return false;
    }
    if (this->operation_type != other.operation_type) {
      return false;
    }
    if (this->ye != other.ye) {
      return false;
    }
    if (this->pos != other.pos) {
      return false;
    }
    if (this->input_source != other.input_source) {
      return false;
    }
    if (this->tau != other.tau) {
      return false;
    }
    return true;
  }
  bool operator!=(const InputTau_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct InputTau_

// alias to use template instance with default allocator
using InputTau =
  px4_msgs::msg::InputTau_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__INPUT_TAU__STRUCT_HPP_
