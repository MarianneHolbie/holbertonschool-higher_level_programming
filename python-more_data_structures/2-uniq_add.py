#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_my_list = list(set(my_list))
    result = 0
    for element in set_my_list:
        result += element
    return (result)
