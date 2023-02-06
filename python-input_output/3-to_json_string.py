#!/usr/bin/python3
"""
    Module contain function that return the JSON representation
"""


import json


def to_json_string(my_obj):
    """
        function to return the JSON representation of an object

        Attribut:
        ==================

            my_obj : objet to convert
    """

    return (json.dumps(my_obj))
