#!/usr/bin/python3
""" This module is a first creation of class that define a square """


class Square():
    """
    Class that defines a square

    Attributes
    ----------
    __size : size of the square, private attributes

    """

    def __init__(self, __size=0):
        if type(__size) != int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
