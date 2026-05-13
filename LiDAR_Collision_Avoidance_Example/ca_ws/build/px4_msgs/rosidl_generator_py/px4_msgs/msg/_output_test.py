# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/OutputTest.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'sates'
# Member 'command'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_OutputTest(type):
    """Metaclass of message 'OutputTest'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('px4_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'px4_msgs.msg.OutputTest')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__output_test
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__output_test
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__output_test
            cls._TYPE_SUPPORT = module.type_support_msg__msg__output_test
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__output_test

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class OutputTest(metaclass=Metaclass_OutputTest):
    """Message class 'OutputTest'."""

    __slots__ = [
        '_timestamp',
        '_timestamp_last_signal',
        '_sates',
        '_command',
        '_estimated_d',
        '_eso_type',
        '_nomoto_t',
        '_nomoto_k',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'timestamp_last_signal': 'uint64',
        'sates': 'double[9]',
        'command': 'double[7]',
        'estimated_d': 'double',
        'eso_type': 'int8',
        'nomoto_t': 'float',
        'nomoto_k': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 9),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 7),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.timestamp_last_signal = kwargs.get('timestamp_last_signal', int())
        if 'sates' not in kwargs:
            self.sates = numpy.zeros(9, dtype=numpy.float64)
        else:
            self.sates = kwargs.get('sates')
        if 'command' not in kwargs:
            self.command = numpy.zeros(7, dtype=numpy.float64)
        else:
            self.command = kwargs.get('command')
        self.estimated_d = kwargs.get('estimated_d', float())
        self.eso_type = kwargs.get('eso_type', int())
        self.nomoto_t = kwargs.get('nomoto_t', float())
        self.nomoto_k = kwargs.get('nomoto_k', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.timestamp_last_signal != other.timestamp_last_signal:
            return False
        if any(self.sates != other.sates):
            return False
        if any(self.command != other.command):
            return False
        if self.estimated_d != other.estimated_d:
            return False
        if self.eso_type != other.eso_type:
            return False
        if self.nomoto_t != other.nomoto_t:
            return False
        if self.nomoto_k != other.nomoto_k:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp = value

    @builtins.property
    def timestamp_last_signal(self):
        """Message field 'timestamp_last_signal'."""
        return self._timestamp_last_signal

    @timestamp_last_signal.setter
    def timestamp_last_signal(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp_last_signal' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp_last_signal' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp_last_signal = value

    @builtins.property
    def sates(self):
        """Message field 'sates'."""
        return self._sates

    @sates.setter
    def sates(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'sates' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 9, \
                "The 'sates' numpy.ndarray() must have a size of 9"
            self._sates = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 9 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'sates' field must be a set or sequence with length 9 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._sates = numpy.array(value, dtype=numpy.float64)

    @builtins.property
    def command(self):
        """Message field 'command'."""
        return self._command

    @command.setter
    def command(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'command' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 7, \
                "The 'command' numpy.ndarray() must have a size of 7"
            self._command = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 7 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'command' field must be a set or sequence with length 7 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._command = numpy.array(value, dtype=numpy.float64)

    @builtins.property
    def estimated_d(self):
        """Message field 'estimated_d'."""
        return self._estimated_d

    @estimated_d.setter
    def estimated_d(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'estimated_d' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'estimated_d' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._estimated_d = value

    @builtins.property
    def eso_type(self):
        """Message field 'eso_type'."""
        return self._eso_type

    @eso_type.setter
    def eso_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'eso_type' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'eso_type' field must be an integer in [-128, 127]"
        self._eso_type = value

    @builtins.property
    def nomoto_t(self):
        """Message field 'nomoto_t'."""
        return self._nomoto_t

    @nomoto_t.setter
    def nomoto_t(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'nomoto_t' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'nomoto_t' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._nomoto_t = value

    @builtins.property
    def nomoto_k(self):
        """Message field 'nomoto_k'."""
        return self._nomoto_k

    @nomoto_k.setter
    def nomoto_k(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'nomoto_k' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'nomoto_k' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._nomoto_k = value
