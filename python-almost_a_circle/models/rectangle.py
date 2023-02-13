#!/usr/bin/python3
"""
    inheritance class
"""

from models.base import Base


class Rectangle(Base):
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
        if isinstance(width, int):
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError('width must be > 0')
        if isinstance(height, int):
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError('height must be > 0')
        if isinstance(x, int):
            if x < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = x
        else:
            raise TypeError("x must be an integer")

        if isinstance(y, int):
            if y < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__y = y
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.__x = value
        else:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.__y = value
        else:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')