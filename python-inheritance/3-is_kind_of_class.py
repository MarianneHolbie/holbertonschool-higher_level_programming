#!/usr/bin/python3
"""
    Module to test if same class of inherit from
    
"""


def is_kind_of_class(obj, a_class):
    """
        return True if object instance of specified class of or
        instance of class inherited from specified class
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
