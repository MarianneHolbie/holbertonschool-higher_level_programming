#!/usr/bin/python3
"""
    Module to append string at the end of text file
"""


def append_write(filename="", text=""):
    """
        function that appends a string at the end of file
        return number char added

        Attributs:
        =================

            filename : name of file to append

            text : text to add
    """
    with open(filename, "a", encoding="utf-8") as f:
        value = f.write(''.join(text))
        return (value)
