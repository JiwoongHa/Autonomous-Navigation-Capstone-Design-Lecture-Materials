// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from px4_msgs:msg/CommandValues.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "px4_msgs/msg/detail/command_values__struct.h"
#include "px4_msgs/msg/detail/command_values__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool px4_msgs__msg__command_values__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[43];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("px4_msgs.msg._command_values.CommandValues", full_classname_dest, 42) == 0);
  }
  px4_msgs__msg__CommandValues * ros_message = _ros_message;
  {  // timestamp
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // rc_on_off_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "rc_on_off_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->rc_on_off_log = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // d_mode_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "d_mode_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->d_mode_log = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // wp_mode_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "wp_mode_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->wp_mode_log = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // u_cmd_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "u_cmd_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->u_cmd_log = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // x_cmd_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_cmd_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_cmd_log = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_cmd_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_cmd_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_cmd_log = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // psi_cmd_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "psi_cmd_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->psi_cmd_log = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ye_log
    PyObject * field = PyObject_GetAttrString(_pymsg, "ye_log");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ye_log = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // x_berth_start
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_berth_start");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_berth_start = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_berth_start
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_berth_start");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_berth_start = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // x_berth_end
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_berth_end");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_berth_end = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_berth_end
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_berth_end");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_berth_end = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * px4_msgs__msg__command_values__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of CommandValues */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("px4_msgs.msg._command_values");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "CommandValues");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  px4_msgs__msg__CommandValues * ros_message = (px4_msgs__msg__CommandValues *)raw_ros_message;
  {  // timestamp
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->timestamp);
    {
      int rc = PyObject_SetAttrString(_pymessage, "timestamp", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rc_on_off_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->rc_on_off_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rc_on_off_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // d_mode_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->d_mode_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "d_mode_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // wp_mode_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->wp_mode_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "wp_mode_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // u_cmd_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->u_cmd_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "u_cmd_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_cmd_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_cmd_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_cmd_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_cmd_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_cmd_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_cmd_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // psi_cmd_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->psi_cmd_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "psi_cmd_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ye_log
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ye_log);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ye_log", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_berth_start
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_berth_start);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_berth_start", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_berth_start
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_berth_start);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_berth_start", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_berth_end
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_berth_end);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_berth_end", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_berth_end
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_berth_end);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_berth_end", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
