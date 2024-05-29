#!/usr/bin/python3
"""containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """returns True if the ojt is an instance of, or if the
    ojt is an instance of a class that inherited from
    the specified class ; False """
    return isinstance(obj, a_class)
