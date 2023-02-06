#!/usr/bin/python3
"""
    Module to test only subclass
"""


def inherits_from(obj, a_class):
    """
        function return true if object is an instance of a class that
        inherate (directly or indirectly specified class)
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
