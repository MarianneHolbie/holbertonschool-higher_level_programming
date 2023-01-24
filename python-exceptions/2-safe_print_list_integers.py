#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in range(0, x):
        # try to print : ok if element is number
        try:
            print("{:d}".format(my_list[element]), end='')
            count += 1

        # except error of type, index : but go through
        except (TypeError, ValueError, IndexError):
            pass
    print()
    return (count)
