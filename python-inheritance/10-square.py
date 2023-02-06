#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle.
"""
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
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)

    def area(self):
        """
            calculate area of square

        """
        result = self.__size ** 2
        return (result)
