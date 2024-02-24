#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Class representing a rectangle with width and height properties."""

    def __init__(self, width=0, height=0):
        """Creates a new instance of Rectangle with optional width and height."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriever."""
        return self.__width

    @property
    def height(self):
        """Height retriever."""
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for the width."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for the height."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter."""
        return 2 * (self.__height + self.__width) if self.__height > 0 and self.width > 0 else 0

    def __str__(self):
        """Returns a string representation."""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation."""
        return f"Rectangle({self.__width}, {self.__height})"
