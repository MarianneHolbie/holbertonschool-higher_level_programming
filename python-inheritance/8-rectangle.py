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

    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
