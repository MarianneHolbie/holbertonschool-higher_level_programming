#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_a_dictionary = dict(sorted(a_dictionary.items()))
    for key, value in sort_a_dictionary.items():
        print("{}: {}".format(key, value))
