#!/usr/bin/python3
"""
    Package Base class

"""
import json
from pathlib import Path


class Base:
    """
        Base class

        ATTRIBUTS
        ==================
            __nb_objects : private, count

            id : id of each form

        METHOD
        ==================

            @classMethod:

                save_to_file : write json string in list_dictionary

                create: create instance of subclasse and update
                        value with **dict

                load_from_file: load file of instance subclass, extract
                                form and create

            @StaticMethod:

                to_json_string : static method to return json string
                                 representation

                from_json_string : return list of the JSON string
                                   representation json_string

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            constructor of base class
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
        dummy.x = 0
        dummy.y = 0
        # update value
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
            return list of instance
        """
        # generate name of file
        filename = '{}.json'.format(cls.__name__)
        path = Path('./' + filename)
        # empty struct : dict and list
        form_list = []
        list_form = []
        # test if file exist
        if path.is_file():
            with open(filename, "r", encoding="utf-8") as f:
                list_elements = f.read()
                form_list = cls.from_json_string(list_elements)
            for k in form_list:
                new_form = cls.create(**k)
                list_form.append(new_form)
            return (list_form)
        else:
            return ([])
