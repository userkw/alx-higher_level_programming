#!/usr/bin/python3
"""Defines an int addition func"""


def add_integer(a, b=98):
    """Return the int addition of a and b.

    Float argts are typecasted to ints before addition is performed

    Raises:
        TypeError: If either of a or b is a non-int and non-flt
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
