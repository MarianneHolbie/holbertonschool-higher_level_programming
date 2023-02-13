#!/usr/bin/python3
"""
    class Square inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        subclass of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            constructeur
        """
        super().__init__(height=size, width=size, x=x, y=y, id=id)
