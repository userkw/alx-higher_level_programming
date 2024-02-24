#!/usr/bin/python3

class Rectangle:
    """class that defines a rect

    Attributes:
        width (int): Width of the rect
        height (int): Height of the rect
    """
    def __init__(self, width=0, height=0):
        """init a new Rect

        Args:
            width (int, optional): width of the rect
            height (int, optional): height of the rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height of rect."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of a rect."""
        return self.__height * self.__width

    def perimeter(self):
        """calculates peri"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """prints the rect"""
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
        """returns a str"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a mesg"""
        print("Bye rectangle...")

# Test the class
if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
