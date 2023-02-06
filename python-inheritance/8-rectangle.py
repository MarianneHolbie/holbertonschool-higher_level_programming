#!/usr/bin/python3
"""
    Module to define class BaseGeometry objects and subclass Rectangle
"""


class BaseGeometry:
    """
        base class BaseGeometry

        Method
        ====================

            area : methode not implemented yet

            integer_validator : check value

    """

    def area(self):
        """
            find area

        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            check value type

            Attributs
            ===========

                name : string
                value : value to check

        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
        inherate class of BaseGeometry

        Attributs
        ====================

            __width : width of the form
                private

            __height : height of the form
                private

    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
