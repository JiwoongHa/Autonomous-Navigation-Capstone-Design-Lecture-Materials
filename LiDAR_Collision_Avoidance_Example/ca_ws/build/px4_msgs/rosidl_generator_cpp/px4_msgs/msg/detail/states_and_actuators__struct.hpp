// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__StatesAndActuators __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__StatesAndActuators __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StatesAndActuators_
{
  using Type = StatesAndActuators_<ContainerAllocator>;

  explicit StatesAndActuators_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->u_time_log = 0.0;
      this->v_time_log = 0.0;
      this->r_time_log = 0.0;
      this->x_time_log = 0.0;
      this->y_time_log = 0.0;
      this->psi_time_log = 0.0;
      this->taux_time_log = 0.0;
      this->tauy_time_log = 0.0;
      this->taun_time_log = 0.0;
      this->motor1_time_log = 0.0;
      this->motor2_time_log = 0.0;
      this->motor3_time_log = 0.0;
      this->motor4_time_log = 0.0;
      this->alpha1_time_log = 0.0;
      this->alpha2_time_log = 0.0;
      this->alpha3_time_log = 0.0;
      this->alpha4_time_log = 0.0;
    }
  }

  explicit StatesAndActuators_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->u_time_log = 0.0;
      this->v_time_log = 0.0;
      this->r_time_log = 0.0;
      this->x_time_log = 0.0;
      this->y_time_log = 0.0;
      this->psi_time_log = 0.0;
      this->taux_time_log = 0.0;
      this->tauy_time_log = 0.0;
      this->taun_time_log = 0.0;
      this->motor1_time_log = 0.0;
      this->motor2_time_log = 0.0;
      this->motor3_time_log = 0.0;
      this->motor4_time_log = 0.0;
      this->alpha1_time_log = 0.0;
      this->alpha2_time_log = 0.0;
      this->alpha3_time_log = 0.0;
      this->alpha4_time_log = 0.0;
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _u_time_log_type =
    double;
  _u_time_log_type u_time_log;
  using _v_time_log_type =
    double;
  _v_time_log_type v_time_log;
  using _r_time_log_type =
    double;
  _r_time_log_type r_time_log;
  using _x_time_log_type =
    double;
  _x_time_log_type x_time_log;
  using _y_time_log_type =
    double;
  _y_time_log_type y_time_log;
  using _psi_time_log_type =
    double;
  _psi_time_log_type psi_time_log;
  using _taux_time_log_type =
    double;
  _taux_time_log_type taux_time_log;
  using _tauy_time_log_type =
    double;
  _tauy_time_log_type tauy_time_log;
  using _taun_time_log_type =
    double;
  _taun_time_log_type taun_time_log;
  using _motor1_time_log_type =
    double;
  _motor1_time_log_type motor1_time_log;
  using _motor2_time_log_type =
    double;
  _motor2_time_log_type motor2_time_log;
  using _motor3_time_log_type =
    double;
  _motor3_time_log_type motor3_time_log;
  using _motor4_time_log_type =
    double;
  _motor4_time_log_type motor4_time_log;
  using _alpha1_time_log_type =
    double;
  _alpha1_time_log_type alpha1_time_log;
  using _alpha2_time_log_type =
    double;
  _alpha2_time_log_type alpha2_time_log;
  using _alpha3_time_log_type =
    double;
  _alpha3_time_log_type alpha3_time_log;
  using _alpha4_time_log_type =
    double;
  _alpha4_time_log_type alpha4_time_log;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__u_time_log(
    const double & _arg)
  {
    this->u_time_log = _arg;
    return *this;
  }
  Type & set__v_time_log(
    const double & _arg)
  {
    this->v_time_log = _arg;
    return *this;
  }
  Type & set__r_time_log(
    const double & _arg)
  {
    this->r_time_log = _arg;
    return *this;
  }
  Type & set__x_time_log(
    const double & _arg)
  {
    this->x_time_log = _arg;
    return *this;
  }
  Type & set__y_time_log(
    const double & _arg)
  {
    this->y_time_log = _arg;
    return *this;
  }
  Type & set__psi_time_log(
    const double & _arg)
  {
    this->psi_time_log = _arg;
    return *this;
  }
  Type & set__taux_time_log(
    const double & _arg)
  {
    this->taux_time_log = _arg;
    return *this;
  }
  Type & set__tauy_time_log(
    const double & _arg)
  {
    this->tauy_time_log = _arg;
    return *this;
  }
  Type & set__taun_time_log(
    const double & _arg)
  {
    this->taun_time_log = _arg;
    return *this;
  }
  Type & set__motor1_time_log(
    const double & _arg)
  {
    this->motor1_time_log = _arg;
    return *this;
  }
  Type & set__motor2_time_log(
    const double & _arg)
  {
    this->motor2_time_log = _arg;
    return *this;
  }
  Type & set__motor3_time_log(
    const double & _arg)
  {
    this->motor3_time_log = _arg;
    return *this;
  }
  Type & set__motor4_time_log(
    const double & _arg)
  {
    this->motor4_time_log = _arg;
    return *this;
  }
  Type & set__alpha1_time_log(
    const double & _arg)
  {
    this->alpha1_time_log = _arg;
    return *this;
  }
  Type & set__alpha2_time_log(
    const double & _arg)
  {
    this->alpha2_time_log = _arg;
    return *this;
  }
  Type & set__alpha3_time_log(
    const double & _arg)
  {
    this->alpha3_time_log = _arg;
    return *this;
  }
  Type & set__alpha4_time_log(
    const double & _arg)
  {
    this->alpha4_time_log = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::StatesAndActuators_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::StatesAndActuators_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::StatesAndActuators_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::StatesAndActuators_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__StatesAndActuators
    std::shared_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__StatesAndActuators
    std::shared_ptr<px4_msgs::msg::StatesAndActuators_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StatesAndActuators_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->u_time_log != other.u_time_log) {
      return false;
    }
    if (this->v_time_log != other.v_time_log) {
      return false;
    }
    if (this->r_time_log != other.r_time_log) {
      return false;
    }
    if (this->x_time_log != other.x_time_log) {
      return false;
    }
    if (this->y_time_log != other.y_time_log) {
      return false;
    }
    if (this->psi_time_log != other.psi_time_log) {
      return false;
    }
    if (this->taux_time_log != other.taux_time_log) {
      return false;
    }
    if (this->tauy_time_log != other.tauy_time_log) {
      return false;
    }
    if (this->taun_time_log != other.taun_time_log) {
      return false;
    }
    if (this->motor1_time_log != other.motor1_time_log) {
      return false;
    }
    if (this->motor2_time_log != other.motor2_time_log) {
      return false;
    }
    if (this->motor3_time_log != other.motor3_time_log) {
      return false;
    }
    if (this->motor4_time_log != other.motor4_time_log) {
      return false;
    }
    if (this->alpha1_time_log != other.alpha1_time_log) {
      return false;
    }
    if (this->alpha2_time_log != other.alpha2_time_log) {
      return false;
    }
    if (this->alpha3_time_log != other.alpha3_time_log) {
      return false;
    }
    if (this->alpha4_time_log != other.alpha4_time_log) {
      return false;
    }
    return true;
  }
  bool operator!=(const StatesAndActuators_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StatesAndActuators_

// alias to use template instance with default allocator
using StatesAndActuators =
  px4_msgs::msg::StatesAndActuators_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__STATES_AND_ACTUATORS__STRUCT_HPP_
