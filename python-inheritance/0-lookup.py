#!/usr/bin/python3
"""
    Lookup in an object
"""


def lookup(obj):
    """
        function that return list of available attributes and
        methods of an object

        Attributs
        ------------------

            obj: object to look inside

    """
    return (dir(obj))
