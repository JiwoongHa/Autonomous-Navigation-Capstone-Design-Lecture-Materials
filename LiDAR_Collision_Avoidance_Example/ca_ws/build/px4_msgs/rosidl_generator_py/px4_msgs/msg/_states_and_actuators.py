# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/StatesAndActuators.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StatesAndActuators(type):
    """Metaclass of message 'StatesAndActuators'."""

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
                'px4_msgs.msg.StatesAndActuators')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__states_and_actuators
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__states_and_actuators
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__states_and_actuators
            cls._TYPE_SUPPORT = module.type_support_msg__msg__states_and_actuators
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__states_and_actuators

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StatesAndActuators(metaclass=Metaclass_StatesAndActuators):
    """Message class 'StatesAndActuators'."""

    __slots__ = [
        '_timestamp',
        '_u_time_log',
        '_v_time_log',
        '_r_time_log',
        '_x_time_log',
        '_y_time_log',
        '_psi_time_log',
        '_taux_time_log',
        '_tauy_time_log',
        '_taun_time_log',
        '_motor1_time_log',
        '_motor2_time_log',
        '_motor3_time_log',
        '_motor4_time_log',
        '_alpha1_time_log',
        '_alpha2_time_log',
        '_alpha3_time_log',
        '_alpha4_time_log',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'u_time_log': 'double',
        'v_time_log': 'double',
        'r_time_log': 'double',
        'x_time_log': 'double',
        'y_time_log': 'double',
        'psi_time_log': 'double',
        'taux_time_log': 'double',
        'tauy_time_log': 'double',
        'taun_time_log': 'double',
        'motor1_time_log': 'double',
        'motor2_time_log': 'double',
        'motor3_time_log': 'double',
        'motor4_time_log': 'double',
        'alpha1_time_log': 'double',
        'alpha2_time_log': 'double',
        'alpha3_time_log': 'double',
        'alpha4_time_log': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
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
        self.u_time_log = kwargs.get('u_time_log', float())
        self.v_time_log = kwargs.get('v_time_log', float())
        self.r_time_log = kwargs.get('r_time_log', float())
        self.x_time_log = kwargs.get('x_time_log', float())
        self.y_time_log = kwargs.get('y_time_log', float())
        self.psi_time_log = kwargs.get('psi_time_log', float())
        self.taux_time_log = kwargs.get('taux_time_log', float())
        self.tauy_time_log = kwargs.get('tauy_time_log', float())
        self.taun_time_log = kwargs.get('taun_time_log', float())
        self.motor1_time_log = kwargs.get('motor1_time_log', float())
        self.motor2_time_log = kwargs.get('motor2_time_log', float())
        self.motor3_time_log = kwargs.get('motor3_time_log', float())
        self.motor4_time_log = kwargs.get('motor4_time_log', float())
        self.alpha1_time_log = kwargs.get('alpha1_time_log', float())
        self.alpha2_time_log = kwargs.get('alpha2_time_log', float())
        self.alpha3_time_log = kwargs.get('alpha3_time_log', float())
        self.alpha4_time_log = kwargs.get('alpha4_time_log', float())

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
        if self.u_time_log != other.u_time_log:
            return False
        if self.v_time_log != other.v_time_log:
            return False
        if self.r_time_log != other.r_time_log:
            return False
        if self.x_time_log != other.x_time_log:
            return False
        if self.y_time_log != other.y_time_log:
            return False
        if self.psi_time_log != other.psi_time_log:
            return False
        if self.taux_time_log != other.taux_time_log:
            return False
        if self.tauy_time_log != other.tauy_time_log:
            return False
        if self.taun_time_log != other.taun_time_log:
            return False
        if self.motor1_time_log != other.motor1_time_log:
            return False
        if self.motor2_time_log != other.motor2_time_log:
            return False
        if self.motor3_time_log != other.motor3_time_log:
            return False
        if self.motor4_time_log != other.motor4_time_log:
            return False
        if self.alpha1_time_log != other.alpha1_time_log:
            return False
        if self.alpha2_time_log != other.alpha2_time_log:
            return False
        if self.alpha3_time_log != other.alpha3_time_log:
            return False
        if self.alpha4_time_log != other.alpha4_time_log:
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
    def u_time_log(self):
        """Message field 'u_time_log'."""
        return self._u_time_log

    @u_time_log.setter
    def u_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'u_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'u_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._u_time_log = value

    @builtins.property
    def v_time_log(self):
        """Message field 'v_time_log'."""
        return self._v_time_log

    @v_time_log.setter
    def v_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'v_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'v_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._v_time_log = value

    @builtins.property
    def r_time_log(self):
        """Message field 'r_time_log'."""
        return self._r_time_log

    @r_time_log.setter
    def r_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'r_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'r_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._r_time_log = value

    @builtins.property
    def x_time_log(self):
        """Message field 'x_time_log'."""
        return self._x_time_log

    @x_time_log.setter
    def x_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_time_log = value

    @builtins.property
    def y_time_log(self):
        """Message field 'y_time_log'."""
        return self._y_time_log

    @y_time_log.setter
    def y_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_time_log = value

    @builtins.property
    def psi_time_log(self):
        """Message field 'psi_time_log'."""
        return self._psi_time_log

    @psi_time_log.setter
    def psi_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'psi_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'psi_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._psi_time_log = value

    @builtins.property
    def taux_time_log(self):
        """Message field 'taux_time_log'."""
        return self._taux_time_log

    @taux_time_log.setter
    def taux_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'taux_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'taux_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._taux_time_log = value

    @builtins.property
    def tauy_time_log(self):
        """Message field 'tauy_time_log'."""
        return self._tauy_time_log

    @tauy_time_log.setter
    def tauy_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tauy_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tauy_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tauy_time_log = value

    @builtins.property
    def taun_time_log(self):
        """Message field 'taun_time_log'."""
        return self._taun_time_log

    @taun_time_log.setter
    def taun_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'taun_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'taun_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._taun_time_log = value

    @builtins.property
    def motor1_time_log(self):
        """Message field 'motor1_time_log'."""
        return self._motor1_time_log

    @motor1_time_log.setter
    def motor1_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'motor1_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'motor1_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._motor1_time_log = value

    @builtins.property
    def motor2_time_log(self):
        """Message field 'motor2_time_log'."""
        return self._motor2_time_log

    @motor2_time_log.setter
    def motor2_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'motor2_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'motor2_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._motor2_time_log = value

    @builtins.property
    def motor3_time_log(self):
        """Message field 'motor3_time_log'."""
        return self._motor3_time_log

    @motor3_time_log.setter
    def motor3_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'motor3_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'motor3_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._motor3_time_log = value

    @builtins.property
    def motor4_time_log(self):
        """Message field 'motor4_time_log'."""
        return self._motor4_time_log

    @motor4_time_log.setter
    def motor4_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'motor4_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'motor4_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._motor4_time_log = value

    @builtins.property
    def alpha1_time_log(self):
        """Message field 'alpha1_time_log'."""
        return self._alpha1_time_log

    @alpha1_time_log.setter
    def alpha1_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alpha1_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'alpha1_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._alpha1_time_log = value

    @builtins.property
    def alpha2_time_log(self):
        """Message field 'alpha2_time_log'."""
        return self._alpha2_time_log

    @alpha2_time_log.setter
    def alpha2_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alpha2_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'alpha2_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._alpha2_time_log = value

    @builtins.property
    def alpha3_time_log(self):
        """Message field 'alpha3_time_log'."""
        return self._alpha3_time_log

    @alpha3_time_log.setter
    def alpha3_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alpha3_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'alpha3_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._alpha3_time_log = value

    @builtins.property
    def alpha4_time_log(self):
        """Message field 'alpha4_time_log'."""
        return self._alpha4_time_log

    @alpha4_time_log.setter
    def alpha4_time_log(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alpha4_time_log' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'alpha4_time_log' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._alpha4_time_log = value
