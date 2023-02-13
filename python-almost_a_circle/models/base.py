#!/usr/bin/python3
"""
    Package Base class

"""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            return JSON string representation of list_dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
            write Json string representation of list_obj in a file
        """
        filename = '{}.json'.format(cls.__name__)
        resume_list = []

        if not list_objs or list_objs is None:
            resume_list = []
        else:
            for elmt in list_objs:
                resume_list.append(elmt.to_dictionary())

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(resume_list))

    @staticmethod
    def from_json_string(json_string):
        """
            return list of the JSON string representation json_string
        """
        if not json_string or json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
        """
        # create dummy form: square 2*2
        dummy = cls(2, 2)
        # update value
        dummy.update(**dictionary)
        return (dummy)
