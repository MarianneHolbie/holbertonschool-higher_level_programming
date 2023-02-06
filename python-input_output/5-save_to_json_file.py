#!/usr/bin/python3
"""
    Module contain function that save object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
        function that write an Object to a text file
        using JSON representation

        Attribut:
        ==================

            my_obj : obj

            filename : file where write
    """

    with open(filename, "w", encoding="utf-8") as f:
        object = json.dump(my_obj, f)
       