#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: the width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: the height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self._height * self._width

    def perimeter(self):
        """Calculates perimeter of a rectangle.

        Returns:
            int: perimeter.
        """
        return 2 * (self._height + self._width) if self._height != 0 and self._width != 0 else 0

    def __str__(self):
        """Prints the rectangle with the character #.

        Returns:
            str: the rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rectangle = ["#" * self._width + "\n" for _ in range(self._height)]
        return "".join(rectangle)
