#!/usr/bin/python3
"""
    class Square inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        subclass of Rectangle

        Attribute
        ---------
            size : size of square
            x andy :position in space of square

        Method
        ---------
            __str__: print definition of square

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            constructeur
        """
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            Rectangle.__width = value
            Rectangle.__height = value
        else:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    def __str__(self):
        """
            function that print definition of square
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y,
                       self.width))
