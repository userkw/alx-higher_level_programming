#!/usr/bin/python3
"""Def Rectangle"""


class Rectangle:
    """
    A Rectangle Class with public class attributes,
    private instance attributes width, height, public methods,
    special methods, static methods and class methods.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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
        """
        Getter of the property value
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter"""
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return Rectangle(size, size)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a str"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a class
        """
        type(self).number_of_instances -= 1
        print("{:s}".format("Bye rectangle..."))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
          Args:
            - rect_1: Rectangle
            - rect_2: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a_1 = rect_1.area()
        a_2 = rect_2.area()

        if a_1 >= a_2:
            return rect_1

        return rect_2
