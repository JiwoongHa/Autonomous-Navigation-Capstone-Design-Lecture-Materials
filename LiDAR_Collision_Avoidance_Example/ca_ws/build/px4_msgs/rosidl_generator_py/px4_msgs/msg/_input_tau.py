# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/InputTau.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'dock_x'
# Member 'dock_y'
# Member 'pos'
# Member 'tau'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_InputTau(type):
    """Metaclass of message 'InputTau'."""

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
                'px4_msgs.msg.InputTau')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__input_tau
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__input_tau
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__input_tau
            cls._TYPE_SUPPORT = module.type_support_msg__msg__input_tau
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__input_tau

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class InputTau(metaclass=Metaclass_InputTau):
    """Message class 'InputTau'."""

    __slots__ = [
        '_timestamp',
        '_timestamp_last_signal',
        '_channel_count',
        '_docking_type',
        '_wp_guid',
        '_docking_guid',
        '_dock_x',
        '_dock_y',
        '_operation_type',
        '_ye',
        '_pos',
        '_input_source',
        '_tau',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'timestamp_last_signal': 'uint64',
        'channel_count': 'uint8',
        'docking_type': 'int8',
        'wp_guid': 'int8',
        'docking_guid': 'int8',
        'dock_x': 'double[2]',
        'dock_y': 'double[2]',
        'operation_type': 'int8',
        'ye': 'double',
        'pos': 'double[3]',
        'input_source': 'uint8',
        'tau': 'double[3]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 2),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 2),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 3),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 3),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.timestamp_last_signal = kwargs.get('timestamp_last_signal', int())
        self.channel_count = kwargs.get('channel_count', int())
        self.docking_type = kwargs.get('docking_type', int())
        self.wp_guid = kwargs.get('wp_guid', int())
        self.docking_guid = kwargs.get('docking_guid', int())
        if 'dock_x' not in kwargs:
            self.dock_x = numpy.zeros(2, dtype=numpy.float64)
        else:
            self.dock_x = kwargs.get('dock_x')
        if 'dock_y' not in kwargs:
            self.dock_y = numpy.zeros(2, dtype=numpy.float64)
        else:
            self.dock_y = kwargs.get('dock_y')
        self.operation_type = kwargs.get('operation_type', int())
        self.ye = kwargs.get('ye', float())
        if 'pos' not in kwargs:
            self.pos = numpy.zeros(3, dtype=numpy.float64)
        else:
            self.pos = kwargs.get('pos')
        self.input_source = kwargs.get('input_source', int())
        if 'tau' not in kwargs:
            self.tau = numpy.zeros(3, dtype=numpy.float64)
        else:
            self.tau = kwargs.get('tau')

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
        if self.channel_count != other.channel_count:
            return False
        if self.docking_type != other.docking_type:
            return False
        if self.wp_guid != other.wp_guid:
            return False
        if self.docking_guid != other.docking_guid:
            return False
        if any(self.dock_x != other.dock_x):
            return False
        if any(self.dock_y != other.dock_y):
            return False
        if self.operation_type != other.operation_type:
            return False
        if self.ye != other.ye:
            return False
        if any(self.pos != other.pos):
            return False
        if self.input_source != other.input_source:
            return False
        if any(self.tau != other.tau):
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
    def channel_count(self):
        """Message field 'channel_count'."""
        return self._channel_count

    @channel_count.setter
    def channel_count(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'channel_count' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'channel_count' field must be an unsigned integer in [0, 255]"
        self._channel_count = value

    @builtins.property
    def docking_type(self):
        """Message field 'docking_type'."""
        return self._docking_type

    @docking_type.setter
    def docking_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'docking_type' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'docking_type' field must be an integer in [-128, 127]"
        self._docking_type = value

    @builtins.property
    def wp_guid(self):
        """Message field 'wp_guid'."""
        return self._wp_guid

    @wp_guid.setter
    def wp_guid(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'wp_guid' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'wp_guid' field must be an integer in [-128, 127]"
        self._wp_guid = value

    @builtins.property
    def docking_guid(self):
        """Message field 'docking_guid'."""
        return self._docking_guid

    @docking_guid.setter
    def docking_guid(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'docking_guid' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'docking_guid' field must be an integer in [-128, 127]"
        self._docking_guid = value

    @builtins.property
    def dock_x(self):
        """Message field 'dock_x'."""
        return self._dock_x

    @dock_x.setter
    def dock_x(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'dock_x' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 2, \
                "The 'dock_x' numpy.ndarray() must have a size of 2"
            self._dock_x = value
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
                 len(value) == 2 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'dock_x' field must be a set or sequence with length 2 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._dock_x = numpy.array(value, dtype=numpy.float64)

    @builtins.property
    def dock_y(self):
        """Message field 'dock_y'."""
        return self._dock_y

    @dock_y.setter
    def dock_y(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'dock_y' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 2, \
                "The 'dock_y' numpy.ndarray() must have a size of 2"
            self._dock_y = value
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
                 len(value) == 2 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'dock_y' field must be a set or sequence with length 2 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._dock_y = numpy.array(value, dtype=numpy.float64)

    @builtins.property
    def operation_type(self):
        """Message field 'operation_type'."""
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'operation_type' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'operation_type' field must be an integer in [-128, 127]"
        self._operation_type = value

    @builtins.property
    def ye(self):
        """Message field 'ye'."""
        return self._ye

    @ye.setter
    def ye(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ye' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ye' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ye = value

    @builtins.property
    def pos(self):
        """Message field 'pos'."""
        return self._pos

    @pos.setter
    def pos(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'pos' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 3, \
                "The 'pos' numpy.ndarray() must have a size of 3"
            self._pos = value
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
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'pos' field must be a set or sequence with length 3 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._pos = numpy.array(value, dtype=numpy.float64)

    @builtins.property
    def input_source(self):
        """Message field 'input_source'."""
        return self._input_source

    @input_source.setter
    def input_source(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'input_source' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'input_source' field must be an unsigned integer in [0, 255]"
        self._input_source = value

    @builtins.property
    def tau(self):
        """Message field 'tau'."""
        return self._tau

    @tau.setter
    def tau(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'tau' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 3, \
                "The 'tau' numpy.ndarray() must have a size of 3"
            self._tau = value
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
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'tau' field must be a set or sequence with length 3 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._tau = numpy.array(value, dtype=numpy.float64)
