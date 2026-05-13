// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from px4_msgs:msg/SimulinkCustomMessage.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/simulink_custom_message__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
px4_msgs__msg__SimulinkCustomMessage__init(px4_msgs__msg__SimulinkCustomMessage * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  // single_a
  // single_b
  // double_a
  // double_b
  return true;
}

void
px4_msgs__msg__SimulinkCustomMessage__fini(px4_msgs__msg__SimulinkCustomMessage * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  // single_a
  // single_b
  // double_a
  // double_b
}

bool
px4_msgs__msg__SimulinkCustomMessage__are_equal(const px4_msgs__msg__SimulinkCustomMessage * lhs, const px4_msgs__msg__SimulinkCustomMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // single_a
  if (lhs->single_a != rhs->single_a) {
    return false;
  }
  // single_b
  if (lhs->single_b != rhs->single_b) {
    return false;
  }
  // double_a
  if (lhs->double_a != rhs->double_a) {
    return false;
  }
  // double_b
  if (lhs->double_b != rhs->double_b) {
    return false;
  }
  return true;
}

bool
px4_msgs__msg__SimulinkCustomMessage__copy(
  const px4_msgs__msg__SimulinkCustomMessage * input,
  px4_msgs__msg__SimulinkCustomMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  output->timestamp = input->timestamp;
  // single_a
  output->single_a = input->single_a;
  // single_b
  output->single_b = input->single_b;
  // double_a
  output->double_a = input->double_a;
  // double_b
  output->double_b = input->double_b;
  return true;
}

px4_msgs__msg__SimulinkCustomMessage *
px4_msgs__msg__SimulinkCustomMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__SimulinkCustomMessage * msg = (px4_msgs__msg__SimulinkCustomMessage *)allocator.allocate(sizeof(px4_msgs__msg__SimulinkCustomMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(px4_msgs__msg__SimulinkCustomMessage));
  bool success = px4_msgs__msg__SimulinkCustomMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
px4_msgs__msg__SimulinkCustomMessage__destroy(px4_msgs__msg__SimulinkCustomMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    px4_msgs__msg__SimulinkCustomMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
px4_msgs__msg__SimulinkCustomMessage__Sequence__init(px4_msgs__msg__SimulinkCustomMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__SimulinkCustomMessage * data = NULL;

  if (size) {
    data = (px4_msgs__msg__SimulinkCustomMessage *)allocator.zero_allocate(size, sizeof(px4_msgs__msg__SimulinkCustomMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = px4_msgs__msg__SimulinkCustomMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        px4_msgs__msg__SimulinkCustomMessage__fini(&data[i - 1]);
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
px4_msgs__msg__SimulinkCustomMessage__Sequence__fini(px4_msgs__msg__SimulinkCustomMessage__Sequence * array)
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
      px4_msgs__msg__SimulinkCustomMessage__fini(&array->data[i]);
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

px4_msgs__msg__SimulinkCustomMessage__Sequence *
px4_msgs__msg__SimulinkCustomMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__SimulinkCustomMessage__Sequence * array = (px4_msgs__msg__SimulinkCustomMessage__Sequence *)allocator.allocate(sizeof(px4_msgs__msg__SimulinkCustomMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = px4_msgs__msg__SimulinkCustomMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
px4_msgs__msg__SimulinkCustomMessage__Sequence__destroy(px4_msgs__msg__SimulinkCustomMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    px4_msgs__msg__SimulinkCustomMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
px4_msgs__msg__SimulinkCustomMessage__Sequence__are_equal(const px4_msgs__msg__SimulinkCustomMessage__Sequence * lhs, const px4_msgs__msg__SimulinkCustomMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!px4_msgs__msg__SimulinkCustomMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
px4_msgs__msg__SimulinkCustomMessage__Sequence__copy(
  const px4_msgs__msg__SimulinkCustomMessage__Sequence * input,
  px4_msgs__msg__SimulinkCustomMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(px4_msgs__msg__SimulinkCustomMessage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    px4_msgs__msg__SimulinkCustomMessage * data =
      (px4_msgs__msg__SimulinkCustomMessage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!px4_msgs__msg__SimulinkCustomMessage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          px4_msgs__msg__SimulinkCustomMessage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!px4_msgs__msg__SimulinkCustomMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
