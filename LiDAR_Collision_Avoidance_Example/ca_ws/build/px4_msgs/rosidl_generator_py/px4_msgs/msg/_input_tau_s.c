// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from px4_msgs:msg/InputTau.idl
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
#include "px4_msgs/msg/detail/input_tau__struct.h"
#include "px4_msgs/msg/detail/input_tau__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool px4_msgs__msg__input_tau__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("px4_msgs.msg._input_tau.InputTau", full_classname_dest, 32) == 0);
  }
  px4_msgs__msg__InputTau * ros_message = _ros_message;
  {  // timestamp
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // timestamp_last_signal
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp_last_signal");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp_last_signal = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // channel_count
    PyObject * field = PyObject_GetAttrString(_pymsg, "channel_count");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->channel_count = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // docking_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "docking_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->docking_type = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // wp_guid
    PyObject * field = PyObject_GetAttrString(_pymsg, "wp_guid");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->wp_guid = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // docking_guid
    PyObject * field = PyObject_GetAttrString(_pymsg, "docking_guid");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->docking_guid = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // dock_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "dock_x");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
      Py_ssize_t size = 2;
      double * dest = ros_message->dock_x;
      for (Py_ssize_t i = 0; i < size; ++i) {
        double tmp = *(npy_float64 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // dock_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "dock_y");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
      Py_ssize_t size = 2;
      double * dest = ros_message->dock_y;
      for (Py_ssize_t i = 0; i < size; ++i) {
        double tmp = *(npy_float64 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // operation_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "operation_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->operation_type = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // ye
    PyObject * field = PyObject_GetAttrString(_pymsg, "ye");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ye = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
      Py_ssize_t size = 3;
      double * dest = ros_message->pos;
      for (Py_ssize_t i = 0; i < size; ++i) {
        double tmp = *(npy_float64 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // input_source
    PyObject * field = PyObject_GetAttrString(_pymsg, "input_source");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->input_source = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tau
    PyObject * field = PyObject_GetAttrString(_pymsg, "tau");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
      Py_ssize_t size = 3;
      double * dest = ros_message->tau;
      for (Py_ssize_t i = 0; i < size; ++i) {
        double tmp = *(npy_float64 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * px4_msgs__msg__input_tau__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of InputTau */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("px4_msgs.msg._input_tau");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "InputTau");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  px4_msgs__msg__InputTau * ros_message = (px4_msgs__msg__InputTau *)raw_ros_message;
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
  {  // timestamp_last_signal
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->timestamp_last_signal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "timestamp_last_signal", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // channel_count
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->channel_count);
    {
      int rc = PyObject_SetAttrString(_pymessage, "channel_count", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // docking_type
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->docking_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "docking_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // wp_guid
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->wp_guid);
    {
      int rc = PyObject_SetAttrString(_pymessage, "wp_guid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // docking_guid
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->docking_guid);
    {
      int rc = PyObject_SetAttrString(_pymessage, "docking_guid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dock_x
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "dock_x");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
    assert(sizeof(npy_float64) == sizeof(double));
    npy_float64 * dst = (npy_float64 *)PyArray_GETPTR1(seq_field, 0);
    double * src = &(ros_message->dock_x[0]);
    memcpy(dst, src, 2 * sizeof(double));
    Py_DECREF(field);
  }
  {  // dock_y
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "dock_y");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
    assert(sizeof(npy_float64) == sizeof(double));
    npy_float64 * dst = (npy_float64 *)PyArray_GETPTR1(seq_field, 0);
    double * src = &(ros_message->dock_y[0]);
    memcpy(dst, src, 2 * sizeof(double));
    Py_DECREF(field);
  }
  {  // operation_type
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->operation_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "operation_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ye
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ye);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ye", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "pos");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
    assert(sizeof(npy_float64) == sizeof(double));
    npy_float64 * dst = (npy_float64 *)PyArray_GETPTR1(seq_field, 0);
    double * src = &(ros_message->pos[0]);
    memcpy(dst, src, 3 * sizeof(double));
    Py_DECREF(field);
  }
  {  // input_source
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->input_source);
    {
      int rc = PyObject_SetAttrString(_pymessage, "input_source", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tau
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "tau");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
    assert(sizeof(npy_float64) == sizeof(double));
    npy_float64 * dst = (npy_float64 *)PyArray_GETPTR1(seq_field, 0);
    double * src = &(ros_message->tau[0]);
    memcpy(dst, src, 3 * sizeof(double));
    Py_DECREF(field);
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
