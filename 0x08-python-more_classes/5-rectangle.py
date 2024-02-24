#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """represent a rect"""

    def __init__(self, width=0, height=0):
        """init a new rectangle.

        Args:
            width (int): width of the new rect.
            height (int): height of the new rect.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get or set the width of the Rect."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get or set the height of the Rect."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the Rect."""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return the printable representation of the rect.

        represents the rectwith the # char.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """str representation of the Rect."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a messag."""
        print("Bye rectangle...")
