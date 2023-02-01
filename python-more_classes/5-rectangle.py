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

            __str__ : methode to print the rectangle with #

            __repr__ : print widht and height of the rectangle

            __del__ : print message if delate a Rectangle

    """

    rectangcount = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.rectangcount += 1

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

    def __str__(self):
        """ Function that print rectangle with # in string format"""
        recthashtag = ""
        if self.__width == 0 or self.__height == 0:
            return (recthashtag)
        else:
            for i in range(self.__height):
                if i < self.__height - 1:
                    recthashtag += "#" * self.__width + "\n"
                else:
                    recthashtag += "#" * self.__width
        return (recthashtag)

    def __repr__(self):
        """ Function that implement string in repr function"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
