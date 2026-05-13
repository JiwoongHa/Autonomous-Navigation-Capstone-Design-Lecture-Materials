# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/SimulinkCustomMessage.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SimulinkCustomMessage(type):
    """Metaclass of message 'SimulinkCustomMessage'."""

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
                'px4_msgs.msg.SimulinkCustomMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__simulink_custom_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__simulink_custom_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__simulink_custom_message
            cls._TYPE_SUPPORT = module.type_support_msg__msg__simulink_custom_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__simulink_custom_message

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SimulinkCustomMessage(metaclass=Metaclass_SimulinkCustomMessage):
    """Message class 'SimulinkCustomMessage'."""

    __slots__ = [
        '_timestamp',
        '_single_a',
        '_single_b',
        '_double_a',
        '_double_b',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'single_a': 'float',
        'single_b': 'float',
        'double_a': 'double',
        'double_b': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.single_a = kwargs.get('single_a', float())
        self.single_b = kwargs.get('single_b', float())
        self.double_a = kwargs.get('double_a', float())
        self.double_b = kwargs.get('double_b', float())

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
        if self.single_a != other.single_a:
            return False
        if self.single_b != other.single_b:
            return False
        if self.double_a != other.double_a:
            return False
        if self.double_b != other.double_b:
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
    def single_a(self):
        """Message field 'single_a'."""
        return self._single_a

    @single_a.setter
    def single_a(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'single_a' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'single_a' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._single_a = value

    @builtins.property
    def single_b(self):
        """Message field 'single_b'."""
        return self._single_b

    @single_b.setter
    def single_b(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'single_b' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'single_b' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._single_b = value

    @builtins.property
    def double_a(self):
        """Message field 'double_a'."""
        return self._double_a

    @double_a.setter
    def double_a(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'double_a' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'double_a' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._double_a = value

    @builtins.property
    def double_b(self):
        """Message field 'double_b'."""
        return self._double_b

    @double_b.setter
    def double_b(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'double_b' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'double_b' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._double_b = value
