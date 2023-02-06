#!/usr/bin/python3
"""
    Function to read a text file and print it
"""


def read_file(filename=""):
    """
        Read and print a file

        Attribut:
        ================

            filename = name of the file

    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
