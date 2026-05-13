// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from px4_msgs:msg/ModeFlag.idl
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
#include "px4_msgs/msg/detail/mode_flag__struct.h"
#include "px4_msgs/msg/detail/mode_flag__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool px4_msgs__msg__mode_flag__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[33];
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
    assert(strncmp("px4_msgs.msg._mode_flag.ModeFlag", full_classname_dest, 32) == 0);
  }
  px4_msgs__msg__ModeFlag * ros_message = _ros_message;
  {  // timestamp
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // modeone
    PyObject * field = PyObject_GetAttrString(_pymsg, "modeone");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modeone = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modetwo
    PyObject * field = PyObject_GetAttrString(_pymsg, "modetwo");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modetwo = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modethree
    PyObject * field = PyObject_GetAttrString(_pymsg, "modethree");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modethree = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modefour
    PyObject * field = PyObject_GetAttrString(_pymsg, "modefour");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modefour = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modefive
    PyObject * field = PyObject_GetAttrString(_pymsg, "modefive");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modefive = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modesix
    PyObject * field = PyObject_GetAttrString(_pymsg, "modesix");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modesix = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modeseven
    PyObject * field = PyObject_GetAttrString(_pymsg, "modeseven");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modeseven = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modeeight
    PyObject * field = PyObject_GetAttrString(_pymsg, "modeeight");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modeeight = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modenine
    PyObject * field = PyObject_GetAttrString(_pymsg, "modenine");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modenine = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // modeten
    PyObject * field = PyObject_GetAttrString(_pymsg, "modeten");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->modeten = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * px4_msgs__msg__mode_flag__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ModeFlag */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("px4_msgs.msg._mode_flag");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ModeFlag");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  px4_msgs__msg__ModeFlag * ros_message = (px4_msgs__msg__ModeFlag *)raw_ros_message;
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
  {  // modeone
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modeone);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modeone", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modetwo
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modetwo);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modetwo", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modethree
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modethree);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modethree", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modefour
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modefour);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modefour", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modefive
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modefive);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modefive", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modesix
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modesix);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modesix", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modeseven
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modeseven);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modeseven", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modeeight
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modeeight);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modeeight", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modenine
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modenine);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modenine", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // modeten
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->modeten);
    {
      int rc = PyObject_SetAttrString(_pymessage, "modeten", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
