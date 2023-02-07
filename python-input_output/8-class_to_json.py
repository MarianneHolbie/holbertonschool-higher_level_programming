#!/usr/bin/python3
"""
    Module to return dictionnary description 
"""


def class_to_json(obj):
    """
        Function to return dict description of JSON serialization object

        Attribut:
        =============

            obj : class of object (list, dictionnary, string, integer, boolean)
    """
    return (obj.__dict__)
