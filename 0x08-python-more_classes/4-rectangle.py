#!/usr/bin/python3
"""Simple rectangle class."""


class Rectangle:
    """
    Rectangle class with specified width and height attr.

    Attributes:
        width (int): width
        height (int): height
    """
    def __init__(self, width=0, height=0):
        """Initializes new Rectangle instances.

        Args:
            width (int, optional): width of rectangle Def 0
            height (int, optional): height of rectangle Def to 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width"""
        return self.__width

    @property
    def height(self):
        """Height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter

        Args:
            value (int): width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter for height of rectangle

        Args:
            value (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area

        Returns:
            int: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of a rect

        Returns:
            int: perimeter
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """rectangle with the character #

        Returns:
            str: the rect
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """str

        Returns:
            str: the rect
        """
        return "Rect({:d}, {:d})".format(self.__width, self.__height)
