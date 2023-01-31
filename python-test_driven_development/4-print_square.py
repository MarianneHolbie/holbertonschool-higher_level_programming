#!/usr/bin/python3
"""
    Fonction that print a square with the character #

"""


def print_square(size):
    """
    Function that prints a square with the character #

    Args :
        size: length of the square

    Return:
        draw square with #

    Raises:
        Test TypeError and ValueError

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    if isinstance(size, float) and size <= 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print('#'*size)
