#!/usr/bin/python3
"""
    Package Base class

"""
import json


class Base:
    """
        Base class

        METHOD
        ==================

            to_json_string : static method to return json string representation

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            constructor
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
            return JSON string representation of list_dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            return ([])
        else:
            return (json.dumps(list_dictionaries))
