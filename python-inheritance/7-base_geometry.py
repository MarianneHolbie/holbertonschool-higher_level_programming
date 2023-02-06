#!/usr/bin/python3
"""
    Module to define class BaseGeometry objects
"""


class BaseGeometry:
    """
        base class BaseGeometry

        Method
        ====================

            area : methode not implemented yet

            integer_validator : check value

    """

    def area(self):
        """
            find area

        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            check value type

            Attributs
            ===========

                name : string
                value : value to check

        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
