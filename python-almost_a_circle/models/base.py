#!/usr/bin/python3
"""
    Package Base class
"""


class Base:
    """
        Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            constructor
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
