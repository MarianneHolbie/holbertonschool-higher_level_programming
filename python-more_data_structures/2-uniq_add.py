#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for element in my_list:
        counter = my_list.count(element)
        if counter == 1:
            result += element
    return (result)
