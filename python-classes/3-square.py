#!/usr/bin/python3
""" This module is a first creation of class that define a square
    with private size"""


class Square():
    """
    Class that defines a square

    Attributes
    ----------
    __size : integer, must be > 0
        size of the square, private attributes

     Methods
    -------
    area() : calculate the area of the square

    """

    def __init__(self, __size=0):
        """ initialize class Square with size and constraint"""
        if type(__size) != int:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size

    def area(self):
        """ calculate the area of square"""
        return (self.__size)**2
