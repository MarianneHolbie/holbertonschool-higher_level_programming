#!/usr/bin/python3
"""
    inheritance class
"""

from models.base import Base


class Rectangle:
    """
        class rectangle inherits from Base

        Attribute
        ---------
            __width : private instance, width of rectangle
            __height : private instance, height of rectangle
            __x and __y : private instance, position in space of rectangle

    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            constructor
        """
        super().__init__()
        if id is not None:
            self.id = id
        else:
            Rectangle.__nb_objects += 1
            self.id = Rectangle.__nb_objects
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
