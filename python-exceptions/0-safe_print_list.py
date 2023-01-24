#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # case of x is null, nothing print
    if x == 0:
        print('')
        return (0)
    try:
        count = 0
        for element in range(0, x):
            print("{:d}".format(my_list[element]), end='')
            count += 1
        print()

    # exception index of out of range
    except IndexError:
        print()
    # return number of element print
    finally:
        return (count)
