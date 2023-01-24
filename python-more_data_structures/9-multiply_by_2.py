#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dic_by2 = {}
    for key, value in a_dictionary.items():
        a_dic_by2[key] = value * 2
    return a_dic_by2
