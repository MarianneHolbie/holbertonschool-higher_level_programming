#!/usr/bin/python3
"""
    Module that create inheritance class
"""


class MyList(list):
    """
        inheritance class of list

        Method
        ---------------

            print_sorted : print list in ascending sort

    """

    def print_sorted(self):
        """
            function that print ascending sort list
        """
        print(sorted(self))
