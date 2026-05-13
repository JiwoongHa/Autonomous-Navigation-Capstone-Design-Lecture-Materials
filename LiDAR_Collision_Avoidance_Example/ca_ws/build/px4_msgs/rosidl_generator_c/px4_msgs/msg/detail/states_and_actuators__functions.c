// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from px4_msgs:msg/StatesAndActuators.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/states_and_actuators__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
px4_msgs__msg__StatesAndActuators__init(px4_msgs__msg__StatesAndActuators * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  // u_time_log
  // v_time_log
  // r_time_log
  // x_time_log
  // y_time_log
  // psi_time_log
  // taux_time_log
  // tauy_time_log
  // taun_time_log
  // motor1_time_log
  // motor2_time_log
  // motor3_time_log
  // motor4_time_log
  // alpha1_time_log
  // alpha2_time_log
  // alpha3_time_log
  // alpha4_time_log
  return true;
}

void
px4_msgs__msg__StatesAndActuators__fini(px4_msgs__msg__StatesAndActuators * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  // u_time_log
  // v_time_log
  // r_time_log
  // x_time_log
  // y_time_log
  // psi_time_log
  // taux_time_log
  // tauy_time_log
  // taun_time_log
  // motor1_time_log
  // motor2_time_log
  // motor3_time_log
  // motor4_time_log
  // alpha1_time_log
  // alpha2_time_log
  // alpha3_time_log
  // alpha4_time_log
}

bool
px4_msgs__msg__StatesAndActuators__are_equal(const px4_msgs__msg__StatesAndActuators * lhs, const px4_msgs__msg__StatesAndActuators * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // u_time_log
  if (lhs->u_time_log != rhs->u_time_log) {
    return false;
  }
  // v_time_log
  if (lhs->v_time_log != rhs->v_time_log) {
    return false;
  }
  // r_time_log
  if (lhs->r_time_log != rhs->r_time_log) {
    return false;
  }
  // x_time_log
  if (lhs->x_time_log != rhs->x_time_log) {
    return false;
  }
  // y_time_log
  if (lhs->y_time_log != rhs->y_time_log) {
    return false;
  }
  // psi_time_log
  if (lhs->psi_time_log != rhs->psi_time_log) {
    return false;
  }
  // taux_time_log
  if (lhs->taux_time_log != rhs->taux_time_log) {
    return false;
  }
  // tauy_time_log
  if (lhs->tauy_time_log != rhs->tauy_time_log) {
    return false;
  }
  // taun_time_log
  if (lhs->taun_time_log != rhs->taun_time_log) {
    return false;
  }
  // motor1_time_log
  if (lhs->motor1_time_log != rhs->motor1_time_log) {
    return false;
  }
  // motor2_time_log
  if (lhs->motor2_time_log != rhs->motor2_time_log) {
    return false;
  }
  // motor3_time_log
  if (lhs->motor3_time_log != rhs->motor3_time_log) {
    return false;
  }
  // motor4_time_log
  if (lhs->motor4_time_log != rhs->motor4_time_log) {
    return false;
  }
  // alpha1_time_log
  if (lhs->alpha1_time_log != rhs->alpha1_time_log) {
    return false;
  }
  // alpha2_time_log
  if (lhs->alpha2_time_log != rhs->alpha2_time_log) {
    return false;
  }
  // alpha3_time_log
  if (lhs->alpha3_time_log != rhs->alpha3_time_log) {
    return false;
  }
  // alpha4_time_log
  if (lhs->alpha4_time_log != rhs->alpha4_time_log) {
    return false;
  }
  return true;
}

bool
px4_msgs__msg__StatesAndActuators__copy(
  const px4_msgs__msg__StatesAndActuators * input,
  px4_msgs__msg__StatesAndActuators * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  output->timestamp = input->timestamp;
  // u_time_log
  output->u_time_log = input->u_time_log;
  // v_time_log
  output->v_time_log = input->v_time_log;
  // r_time_log
  output->r_time_log = input->r_time_log;
  // x_time_log
  output->x_time_log = input->x_time_log;
  // y_time_log
  output->y_time_log = input->y_time_log;
  // psi_time_log
  output->psi_time_log = input->psi_time_log;
  // taux_time_log
  output->taux_time_log = input->taux_time_log;
  // tauy_time_log
  output->tauy_time_log = input->tauy_time_log;
  // taun_time_log
  output->taun_time_log = input->taun_time_log;
  // motor1_time_log
  output->motor1_time_log = input->motor1_time_log;
  // motor2_time_log
  output->motor2_time_log = input->motor2_time_log;
  // motor3_time_log
  output->motor3_time_log = input->motor3_time_log;
  // motor4_time_log
  output->motor4_time_log = input->motor4_time_log;
  // alpha1_time_log
  output->alpha1_time_log = input->alpha1_time_log;
  // alpha2_time_log
  output->alpha2_time_log = input->alpha2_time_log;
  // alpha3_time_log
  output->alpha3_time_log = input->alpha3_time_log;
  // alpha4_time_log
  output->alpha4_time_log = input->alpha4_time_log;
  return true;
}

px4_msgs__msg__StatesAndActuators *
px4_msgs__msg__StatesAndActuators__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__StatesAndActuators * msg = (px4_msgs__msg__StatesAndActuators *)allocator.allocate(sizeof(px4_msgs__msg__StatesAndActuators), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(px4_msgs__msg__StatesAndActuators));
  bool success = px4_msgs__msg__StatesAndActuators__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
px4_msgs__msg__StatesAndActuators__destroy(px4_msgs__msg__StatesAndActuators * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    px4_msgs__msg__StatesAndActuators__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
px4_msgs__msg__StatesAndActuators__Sequence__init(px4_msgs__msg__StatesAndActuators__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__StatesAndActuators * data = NULL;

  if (size) {
    data = (px4_msgs__msg__StatesAndActuators *)allocator.zero_allocate(size, sizeof(px4_msgs__msg__StatesAndActuators), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = px4_msgs__msg__StatesAndActuators__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        px4_msgs__msg__StatesAndActuators__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
px4_msgs__msg__StatesAndActuators__Sequence__fini(px4_msgs__msg__StatesAndActuators__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      px4_msgs__msg__StatesAndActuators__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

px4_msgs__msg__StatesAndActuators__Sequence *
px4_msgs__msg__StatesAndActuators__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__StatesAndActuators__Sequence * array = (px4_msgs__msg__StatesAndActuators__Sequence *)allocator.allocate(sizeof(px4_msgs__msg__StatesAndActuators__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = px4_msgs__msg__StatesAndActuators__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
px4_msgs__msg__StatesAndActuators__Sequence__destroy(px4_msgs__msg__StatesAndActuators__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    px4_msgs__msg__StatesAndActuators__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
px4_msgs__msg__StatesAndActuators__Sequence__are_equal(const px4_msgs__msg__StatesAndActuators__Sequence * lhs, const px4_msgs__msg__StatesAndActuators__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!px4_msgs__msg__StatesAndActuators__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
px4_msgs__msg__StatesAndActuators__Sequence__copy(
  const px4_msgs__msg__StatesAndActuators__Sequence * input,
  px4_msgs__msg__StatesAndActuators__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(px4_msgs__msg__StatesAndActuators);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    px4_msgs__msg__StatesAndActuators * data =
      (px4_msgs__msg__StatesAndActuators *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!px4_msgs__msg__StatesAndActuators__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          px4_msgs__msg__StatesAndActuators__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!px4_msgs__msg__StatesAndActuators__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
