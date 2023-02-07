#!/usr/bin/python3
"""
    Class Student
"""


class Student:
    """
        class that defines a student

        Attributs:
        ================

            first_name : first name of student

            last_name : last name of student

            age: age of student

        Method:
        ===============

            to_json: retrieve dict representation of student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Function to return dict description of JSON serialization object
            only attribute names contained in this list must be retrieved

        """
        liste = {}
        # None : same case as 9-student.py
        if attrs is None:
            return (self.__dict__)
        else:
            # search key value corresponding in dict
            for key, value in self.__dict__.items():
                if key in attrs:
                    liste[key] = value
        return (liste)

    def reload_from_json(self, json):
        """
            Function replace all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key]
