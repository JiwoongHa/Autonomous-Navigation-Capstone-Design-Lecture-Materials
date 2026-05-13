# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/CommandValues.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CommandValues(type):
    """Metaclass of message 'CommandValues'."""

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
                'px4_msgs.msg.CommandValues')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__command_values
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__command_values
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__command_values
            cls._TYPE_SUPPORT = module.type_support_msg__msg__command_values
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__command_values

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CommandValues(metaclass=Metaclass_CommandValues):
    """Message class 'CommandValues'."""

    __slots__ = [
        '_timestamp',
        '_rc_on_off_log',
        '_d_mode_log',
        '_wp_mode_log',
        '_u_cmd_log',
        '_x_cmd_log',
        '_y_cmd_log',
        '_psi_cmd_log',
        '_ye_log',
        '_x_berth_start',
        '_y_berth_start',
        '_x_berth_end',
        '_y_berth_end',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'rc_on_off_log': 'float',
        'd_mode_log': 'float',
        'wp_mode_log': 'float',
        'u_cmd_log': 'double',
        'x_cmd_log': 'double',
        'y_cmd_log': 'double',
        'psi_cmd_log': 'double',
        'ye_log': 'double',
        'x_berth_start': 'double',
        'y_berth_start': 'double',
        'x_berth_end': 'double',
        'y_berth_end': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.rc_on_off_log = kwargs.get('rc_on_off_log', float())
        self.d_mode_log = kwargs.get('d_mode_log', float())
        self.wp_mode_log = kwargs.get('wp_mode_log', float())
        self.u_cmd_log = kwargs.get('u_cmd_log', float())
        self.x_cmd_log = kwargs.get('x_cmd_log', float())
        self.y_cmd_log = kwargs.get('y_cmd_log', float())
        self.psi_cmd_log = kwargs.get('psi_cmd_log', float())
        self.ye_log = kwargs.get('ye_log', float())
        self.x_berth_start = kwargs.get('x_berth_start', float())
        self.y_berth_start = kwargs.get('y_berth_start', float())
        self.x_berth_end = kwargs.get('x_berth_end', float())
        self.y_berth_end = kwargs.get('y_berth_end', float())

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
        if self.rc_on_off_log != other.rc_on_off_log:
            return False
        if self.d_mode_log != other.d_mode_log:
            return False
        if self.wp_mode_log != other.wp_mode_log:
            return False
        if self.u_cmd_log != other.u_cmd_log:
            return False
        if self.x_cmd_log != other.x_cmd_log:
            return False
        if self.y_cmd_log != other.y_cmd_log:
            return False
        if self.psi_cmd_log != other.psi_cmd_log:
            return False
        if self.ye_log != other.ye_log:
            return False
        if self.x_berth_start != other.x_berth_start:
            return False
        if self.y_berth_start != other.y_berth_start:
            return False
        if self.x_berth_end != other.x_berth_end:
            return False
        if self.y_berth_end != other.y_berth_end:
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
    def rc_on_off_log(self):
        """Message field 'rc_on_off_log'."""
        return self._rc_on_off_log

    @rc_on_off_log.setter
    def rc_on_off_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rc_on_off_log' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'rc_on_off_log' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._rc_on_off_log = value

    @builtins.property
    def d_mode_log(self):
        """Message field 'd_mode_log'."""
        return self._d_mode_log

    @d_mode_log.setter
    def d_mode_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'd_mode_log' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'd_mode_log' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._d_mode_log = value

    @builtins.property
    def wp_mode_log(self):
        """Message field 'wp_mode_log'."""
        return self._wp_mode_log

    @wp_mode_log.setter
    def wp_mode_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'wp_mode_log' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'wp_mode_log' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._wp_mode_log = value

    @builtins.property
    def u_cmd_log(self):
        """Message field 'u_cmd_log'."""
        return self._u_cmd_log

    @u_cmd_log.setter
    def u_cmd_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'u_cmd_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'u_cmd_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._u_cmd_log = value

    @builtins.property
    def x_cmd_log(self):
        """Message field 'x_cmd_log'."""
        return self._x_cmd_log

    @x_cmd_log.setter
    def x_cmd_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_cmd_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_cmd_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_cmd_log = value

    @builtins.property
    def y_cmd_log(self):
        """Message field 'y_cmd_log'."""
        return self._y_cmd_log

    @y_cmd_log.setter
    def y_cmd_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_cmd_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_cmd_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_cmd_log = value

    @builtins.property
    def psi_cmd_log(self):
        """Message field 'psi_cmd_log'."""
        return self._psi_cmd_log

    @psi_cmd_log.setter
    def psi_cmd_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'psi_cmd_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'psi_cmd_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._psi_cmd_log = value

    @builtins.property
    def ye_log(self):
        """Message field 'ye_log'."""
        return self._ye_log

    @ye_log.setter
    def ye_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ye_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ye_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ye_log = value

    @builtins.property
    def x_berth_start(self):
        """Message field 'x_berth_start'."""
        return self._x_berth_start

    @x_berth_start.setter
    def x_berth_start(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_berth_start' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_berth_start' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_berth_start = value

    @builtins.property
    def y_berth_start(self):
        """Message field 'y_berth_start'."""
        return self._y_berth_start

    @y_berth_start.setter
    def y_berth_start(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_berth_start' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_berth_start' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_berth_start = value

    @builtins.property
    def x_berth_end(self):
        """Message field 'x_berth_end'."""
        return self._x_berth_end

    @x_berth_end.setter
    def x_berth_end(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_berth_end' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_berth_end' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_berth_end = value

    @builtins.property
    def y_berth_end(self):
        """Message field 'y_berth_end'."""
        return self._y_berth_end

    @y_berth_end.setter
    def y_berth_end(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_berth_end' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_berth_end' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_berth_end = value
