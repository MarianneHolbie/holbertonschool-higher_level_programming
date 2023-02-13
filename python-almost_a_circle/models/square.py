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

    def __str__(self):
        """
            function that print definition of square
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y,
                       self.width))
