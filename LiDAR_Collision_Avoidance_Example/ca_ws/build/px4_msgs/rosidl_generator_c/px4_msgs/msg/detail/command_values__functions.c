// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice
#include "px4_msgs/msg/detail/command_values__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
px4_msgs__msg__CommandValues__init(px4_msgs__msg__CommandValues * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  // rc_on_off_log
  // d_mode_log
  // wp_mode_log
  // u_cmd_log
  // x_cmd_log
  // y_cmd_log
  // psi_cmd_log
  // ye_log
  // x_berth_start
  // y_berth_start
  // x_berth_end
  // y_berth_end
  return true;
}

void
px4_msgs__msg__CommandValues__fini(px4_msgs__msg__CommandValues * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  // rc_on_off_log
  // d_mode_log
  // wp_mode_log
  // u_cmd_log
  // x_cmd_log
  // y_cmd_log
  // psi_cmd_log
  // ye_log
  // x_berth_start
  // y_berth_start
  // x_berth_end
  // y_berth_end
}

bool
px4_msgs__msg__CommandValues__are_equal(const px4_msgs__msg__CommandValues * lhs, const px4_msgs__msg__CommandValues * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // rc_on_off_log
  if (lhs->rc_on_off_log != rhs->rc_on_off_log) {
    return false;
  }
  // d_mode_log
  if (lhs->d_mode_log != rhs->d_mode_log) {
    return false;
  }
  // wp_mode_log
  if (lhs->wp_mode_log != rhs->wp_mode_log) {
    return false;
  }
  // u_cmd_log
  if (lhs->u_cmd_log != rhs->u_cmd_log) {
    return false;
  }
  // x_cmd_log
  if (lhs->x_cmd_log != rhs->x_cmd_log) {
    return false;
  }
  // y_cmd_log
  if (lhs->y_cmd_log != rhs->y_cmd_log) {
    return false;
  }
  // psi_cmd_log
  if (lhs->psi_cmd_log != rhs->psi_cmd_log) {
    return false;
  }
  // ye_log
  if (lhs->ye_log != rhs->ye_log) {
    return false;
  }
  // x_berth_start
  if (lhs->x_berth_start != rhs->x_berth_start) {
    return false;
  }
  // y_berth_start
  if (lhs->y_berth_start != rhs->y_berth_start) {
    return false;
  }
  // x_berth_end
  if (lhs->x_berth_end != rhs->x_berth_end) {
    return false;
  }
  // y_berth_end
  if (lhs->y_berth_end != rhs->y_berth_end) {
    return false;
  }
  return true;
}

bool
px4_msgs__msg__CommandValues__copy(
  const px4_msgs__msg__CommandValues * input,
  px4_msgs__msg__CommandValues * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  output->timestamp = input->timestamp;
  // rc_on_off_log
  output->rc_on_off_log = input->rc_on_off_log;
  // d_mode_log
  output->d_mode_log = input->d_mode_log;
  // wp_mode_log
  output->wp_mode_log = input->wp_mode_log;
  // u_cmd_log
  output->u_cmd_log = input->u_cmd_log;
  // x_cmd_log
  output->x_cmd_log = input->x_cmd_log;
  // y_cmd_log
  output->y_cmd_log = input->y_cmd_log;
  // psi_cmd_log
  output->psi_cmd_log = input->psi_cmd_log;
  // ye_log
  output->ye_log = input->ye_log;
  // x_berth_start
  output->x_berth_start = input->x_berth_start;
  // y_berth_start
  output->y_berth_start = input->y_berth_start;
  // x_berth_end
  output->x_berth_end = input->x_berth_end;
  // y_berth_end
  output->y_berth_end = input->y_berth_end;
  return true;
}

px4_msgs__msg__CommandValues *
px4_msgs__msg__CommandValues__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__CommandValues * msg = (px4_msgs__msg__CommandValues *)allocator.allocate(sizeof(px4_msgs__msg__CommandValues), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(px4_msgs__msg__CommandValues));
  bool success = px4_msgs__msg__CommandValues__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
px4_msgs__msg__CommandValues__destroy(px4_msgs__msg__CommandValues * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    px4_msgs__msg__CommandValues__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
px4_msgs__msg__CommandValues__Sequence__init(px4_msgs__msg__CommandValues__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__CommandValues * data = NULL;

  if (size) {
    data = (px4_msgs__msg__CommandValues *)allocator.zero_allocate(size, sizeof(px4_msgs__msg__CommandValues), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = px4_msgs__msg__CommandValues__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        px4_msgs__msg__CommandValues__fini(&data[i - 1]);
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
px4_msgs__msg__CommandValues__Sequence__fini(px4_msgs__msg__CommandValues__Sequence * array)
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
      px4_msgs__msg__CommandValues__fini(&array->data[i]);
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

px4_msgs__msg__CommandValues__Sequence *
px4_msgs__msg__CommandValues__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  px4_msgs__msg__CommandValues__Sequence * array = (px4_msgs__msg__CommandValues__Sequence *)allocator.allocate(sizeof(px4_msgs__msg__CommandValues__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = px4_msgs__msg__CommandValues__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
px4_msgs__msg__CommandValues__Sequence__destroy(px4_msgs__msg__CommandValues__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    px4_msgs__msg__CommandValues__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
px4_msgs__msg__CommandValues__Sequence__are_equal(const px4_msgs__msg__CommandValues__Sequence * lhs, const px4_msgs__msg__CommandValues__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!px4_msgs__msg__CommandValues__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
px4_msgs__msg__CommandValues__Sequence__copy(
  const px4_msgs__msg__CommandValues__Sequence * input,
  px4_msgs__msg__CommandValues__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(px4_msgs__msg__CommandValues);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    px4_msgs__msg__CommandValues * data =
      (px4_msgs__msg__CommandValues *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!px4_msgs__msg__CommandValues__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          px4_msgs__msg__CommandValues__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!px4_msgs__msg__CommandValues__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
