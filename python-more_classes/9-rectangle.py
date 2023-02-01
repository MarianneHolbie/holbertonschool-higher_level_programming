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
            number_of_instances : number of instance in the class
            print_symbol : symbol use to draw rectangle

        Methode
        --------
            area : calculate area of the rectangle
            perimeter: calculate perimeter of the given rectangle

            __str__ : methode to print the rectangle with #

            __repr__ : print widht and height of the rectangle

            __del__ : print message if delate a Rectangle

          @classmethod
            square : create a square

          @staticmethod
            bigger_or_equal : compare area of two rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    recthashtag += str(self.print_symbol) * self.__width + "\n"
                else:
                    recthashtag += str(self.print_symbol) * self.__width
        return (recthashtag)

    def __repr__(self):
        """ Function that implement string in repr function"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
