#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        inherate class of BaseGeometry

        Attributs
        ====================

            __width : width of the form
                private

            __height : height of the form
                private

        Method
        ====================

            area : calculate area of the rectangle

            __str__ : return description of the rectangle


    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """
            calculate area

        """
        result = self.__width * self.__height
        return (result)

    def __str__(self):
        """
            print rectangle description
        """
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
