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

    __position : tuple position of square

    Methods
    -------
    area() : calculate the area of the square

    my_print() : print square with #
    """

    def __init__(self, size=0, position=(0, 0)):
        """ constructor method """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter method for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter method for size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter method for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter method for size"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or\
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ calculate the area of square"""
        return (self.__size)**2

    def my_print(self):
        """ print the square with #"""
        if self.__size == 0:
            print('')

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
