#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """rectangle class defined by wdth and heght"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of a rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
