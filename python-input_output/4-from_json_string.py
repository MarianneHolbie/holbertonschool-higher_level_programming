#!/usr/bin/python3
"""
    Module contain function that return object represented
    by JSON string
"""


import json


def from_json_string(my_str):
    """
        function to return object corresponding JSON string

        Attribut:
        ==================

            my_str : str to convert
    """

    return (json.loads(my_str))
