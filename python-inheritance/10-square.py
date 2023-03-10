#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        inherate class of Rectangle

        Attributs
        ====================

            __size : size of the square
                private

        Method
        ====================

            area : calculate area of the rectangle
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
            calculate area of square

        """
        result = self.__size ** 2
        return (result)
