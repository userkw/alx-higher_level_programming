#!/usr/bin/python3
"""defines a class rect"""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): nbr of rect.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init new instances.

        Args:
            width (int): width of rect.
            height (int): height of rect.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width."""
        return self.__width

    @property
    def height(self):
        """Height."""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of rect."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter."""
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rect."""
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a str."""
        return "Rect({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a class"""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
