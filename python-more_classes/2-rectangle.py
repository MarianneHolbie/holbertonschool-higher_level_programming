#!/usr/bin/python3
"""
    Module contain one class to define rectangle
"""


class Rectangle():
    """
        Class define a rectangle

        Attribute
        ---------
            __width : private instance, width of rectangle
            __height : private instance, height of the given rectangle

        Methode
        --------
            area : calculate area of the rectangle
            perimeter: calculate perimeter of the given rectangle

    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Function that calculate area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Function that calculate perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))
