#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    for rev_index in range(len(my_list)-1, -1, -1):
        print("{:d}".format(my_list[rev_index]))