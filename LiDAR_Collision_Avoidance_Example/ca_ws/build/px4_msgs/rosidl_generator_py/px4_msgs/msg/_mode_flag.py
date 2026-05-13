# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/ModeFlag.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ModeFlag(type):
    """Metaclass of message 'ModeFlag'."""

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
                'px4_msgs.msg.ModeFlag')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mode_flag
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mode_flag
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mode_flag
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mode_flag
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mode_flag

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ModeFlag(metaclass=Metaclass_ModeFlag):
    """Message class 'ModeFlag'."""

    __slots__ = [
        '_timestamp',
        '_modeone',
        '_modetwo',
        '_modethree',
        '_modefour',
        '_modefive',
        '_modesix',
        '_modeseven',
        '_modeeight',
        '_modenine',
        '_modeten',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'modeone': 'float',
        'modetwo': 'float',
        'modethree': 'float',
        'modefour': 'float',
        'modefive': 'float',
        'modesix': 'float',
        'modeseven': 'float',
        'modeeight': 'float',
        'modenine': 'float',
        'modeten': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.modeone = kwargs.get('modeone', float())
        self.modetwo = kwargs.get('modetwo', float())
        self.modethree = kwargs.get('modethree', float())
        self.modefour = kwargs.get('modefour', float())
        self.modefive = kwargs.get('modefive', float())
        self.modesix = kwargs.get('modesix', float())
        self.modeseven = kwargs.get('modeseven', float())
        self.modeeight = kwargs.get('modeeight', float())
        self.modenine = kwargs.get('modenine', float())
        self.modeten = kwargs.get('modeten', float())

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
        if self.modeone != other.modeone:
            return False
        if self.modetwo != other.modetwo:
            return False
        if self.modethree != other.modethree:
            return False
        if self.modefour != other.modefour:
            return False
        if self.modefive != other.modefive:
            return False
        if self.modesix != other.modesix:
            return False
        if self.modeseven != other.modeseven:
            return False
        if self.modeeight != other.modeeight:
            return False
        if self.modenine != other.modenine:
            return False
        if self.modeten != other.modeten:
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
    def modeone(self):
        """Message field 'modeone'."""
        return self._modeone

    @modeone.setter
    def modeone(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modeone' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modeone' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modeone = value

    @builtins.property
    def modetwo(self):
        """Message field 'modetwo'."""
        return self._modetwo

    @modetwo.setter
    def modetwo(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modetwo' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modetwo' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modetwo = value

    @builtins.property
    def modethree(self):
        """Message field 'modethree'."""
        return self._modethree

    @modethree.setter
    def modethree(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modethree' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modethree' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modethree = value

    @builtins.property
    def modefour(self):
        """Message field 'modefour'."""
        return self._modefour

    @modefour.setter
    def modefour(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modefour' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modefour' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modefour = value

    @builtins.property
    def modefive(self):
        """Message field 'modefive'."""
        return self._modefive

    @modefive.setter
    def modefive(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modefive' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modefive' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modefive = value

    @builtins.property
    def modesix(self):
        """Message field 'modesix'."""
        return self._modesix

    @modesix.setter
    def modesix(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modesix' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modesix' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modesix = value

    @builtins.property
    def modeseven(self):
        """Message field 'modeseven'."""
        return self._modeseven

    @modeseven.setter
    def modeseven(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modeseven' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modeseven' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modeseven = value

    @builtins.property
    def modeeight(self):
        """Message field 'modeeight'."""
        return self._modeeight

    @modeeight.setter
    def modeeight(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modeeight' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modeeight' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modeeight = value

    @builtins.property
    def modenine(self):
        """Message field 'modenine'."""
        return self._modenine

    @modenine.setter
    def modenine(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modenine' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modenine' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modenine = value

    @builtins.property
    def modeten(self):
        """Message field 'modeten'."""
        return self._modeten

    @modeten.setter
    def modeten(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'modeten' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'modeten' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._modeten = value
