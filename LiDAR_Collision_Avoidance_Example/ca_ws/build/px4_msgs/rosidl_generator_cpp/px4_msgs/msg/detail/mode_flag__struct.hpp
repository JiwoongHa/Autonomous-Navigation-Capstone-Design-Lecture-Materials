// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from px4_msgs:msg/ModeFlag.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__MODE_FLAG__STRUCT_HPP_
#define PX4_MSGS__MSG__DETAIL__MODE_FLAG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__px4_msgs__msg__ModeFlag __attribute__((deprecated))
#else
# define DEPRECATED__px4_msgs__msg__ModeFlag __declspec(deprecated)
#endif

namespace px4_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ModeFlag_
{
  using Type = ModeFlag_<ContainerAllocator>;

  explicit ModeFlag_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->modeone = 0.0f;
      this->modetwo = 0.0f;
      this->modethree = 0.0f;
      this->modefour = 0.0f;
      this->modefive = 0.0f;
      this->modesix = 0.0f;
      this->modeseven = 0.0f;
      this->modeeight = 0.0f;
      this->modenine = 0.0f;
      this->modeten = 0.0f;
    }
  }

  explicit ModeFlag_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->timestamp = 0ull;
      this->modeone = 0.0f;
      this->modetwo = 0.0f;
      this->modethree = 0.0f;
      this->modefour = 0.0f;
      this->modefive = 0.0f;
      this->modesix = 0.0f;
      this->modeseven = 0.0f;
      this->modeeight = 0.0f;
      this->modenine = 0.0f;
      this->modeten = 0.0f;
    }
  }

  // field types and members
  using _timestamp_type =
    uint64_t;
  _timestamp_type timestamp;
  using _modeone_type =
    float;
  _modeone_type modeone;
  using _modetwo_type =
    float;
  _modetwo_type modetwo;
  using _modethree_type =
    float;
  _modethree_type modethree;
  using _modefour_type =
    float;
  _modefour_type modefour;
  using _modefive_type =
    float;
  _modefive_type modefive;
  using _modesix_type =
    float;
  _modesix_type modesix;
  using _modeseven_type =
    float;
  _modeseven_type modeseven;
  using _modeeight_type =
    float;
  _modeeight_type modeeight;
  using _modenine_type =
    float;
  _modenine_type modenine;
  using _modeten_type =
    float;
  _modeten_type modeten;

  // setters for named parameter idiom
  Type & set__timestamp(
    const uint64_t & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__modeone(
    const float & _arg)
  {
    this->modeone = _arg;
    return *this;
  }
  Type & set__modetwo(
    const float & _arg)
  {
    this->modetwo = _arg;
    return *this;
  }
  Type & set__modethree(
    const float & _arg)
  {
    this->modethree = _arg;
    return *this;
  }
  Type & set__modefour(
    const float & _arg)
  {
    this->modefour = _arg;
    return *this;
  }
  Type & set__modefive(
    const float & _arg)
  {
    this->modefive = _arg;
    return *this;
  }
  Type & set__modesix(
    const float & _arg)
  {
    this->modesix = _arg;
    return *this;
  }
  Type & set__modeseven(
    const float & _arg)
  {
    this->modeseven = _arg;
    return *this;
  }
  Type & set__modeeight(
    const float & _arg)
  {
    this->modeeight = _arg;
    return *this;
  }
  Type & set__modenine(
    const float & _arg)
  {
    this->modenine = _arg;
    return *this;
  }
  Type & set__modeten(
    const float & _arg)
  {
    this->modeten = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    px4_msgs::msg::ModeFlag_<ContainerAllocator> *;
  using ConstRawPtr =
    const px4_msgs::msg::ModeFlag_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::ModeFlag_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      px4_msgs::msg::ModeFlag_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__px4_msgs__msg__ModeFlag
    std::shared_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__px4_msgs__msg__ModeFlag
    std::shared_ptr<px4_msgs::msg::ModeFlag_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ModeFlag_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->modeone != other.modeone) {
      return false;
    }
    if (this->modetwo != other.modetwo) {
      return false;
    }
    if (this->modethree != other.modethree) {
      return false;
    }
    if (this->modefour != other.modefour) {
      return false;
    }
    if (this->modefive != other.modefive) {
      return false;
    }
    if (this->modesix != other.modesix) {
      return false;
    }
    if (this->modeseven != other.modeseven) {
      return false;
    }
    if (this->modeeight != other.modeeight) {
      return false;
    }
    if (this->modenine != other.modenine) {
      return false;
    }
    if (this->modeten != other.modeten) {
      return false;
    }
    return true;
  }
  bool operator!=(const ModeFlag_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ModeFlag_

// alias to use template instance with default allocator
using ModeFlag =
  px4_msgs::msg::ModeFlag_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace px4_msgs

#endif  // PX4_MSGS__MSG__DETAIL__MODE_FLAG__STRUCT_HPP_
