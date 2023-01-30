#!/usr/bin/python3
""" This module contain only one function that add two integer"""


def add_integer(a, b=98):
    """
    Function that add two integer number
    """
    try:
        return int(a+b)
    except TypeError:
        if type(a) != int:
            return ('a must be an integer')
        elif type(b) != int:
            return ('b must be an integer')
