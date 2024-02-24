#!/usr/bin/python3
"""ddefines a rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): number.
        print_symbol (any): symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init a new Rect.

        Args:
            width (int): The width of the new rect.
            height (int): The height of the new rect.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set."""
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
        """set."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """return."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        m_rec = []
        for i in range(self.__height):
            [m_rec.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                m_rec.append("\n")
        return ("".join(m_rec))

    def __repr__(self):
        """str representation of the rect."""
        m_rec = "Rectangle(" + str(self.__width)
        m_rec += ", " + str(self.__height) + ")"
        return (m_rec)

    def __del__(self):
        """Print msg"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
