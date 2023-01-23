#!/usr/bin/python3
def no_c(my_string):
    list_string = list(my_string)
    new_string = []
    for i in list_string:
        if i == 'c' or i == 'C':
            i = ''
        new_string.append(i)
    return (''.join(new_string))
