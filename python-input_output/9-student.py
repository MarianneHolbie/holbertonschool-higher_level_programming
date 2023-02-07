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

    def to_json(self):
        """
            Function to return dict description of JSON serialization object

        """
        return (self.__dict__)
