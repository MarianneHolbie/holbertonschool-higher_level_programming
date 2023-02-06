#!/usr/bin/python3
"""
    Module to test if an object is instance of specified class
"""


def is_same_class(obj, a_class):
    """
        Function that return True if object is exactly an instance of
        the specified class
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return (True)
    else:
        return (False)
