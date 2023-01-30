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

    def __init__(self, size=0):
        """ constructor method """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """ Getter method for size"""
        return (self.__size)

    def size(self, value):
        """ Setter method for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculate the area of square"""
        return (self.__size)**2
