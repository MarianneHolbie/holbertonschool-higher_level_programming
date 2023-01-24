#!/usr/bin/python3
def safe_print_integer(value):
    # print an integer
    try:
        print("{:d}".format(value))
        return True

    # if is not an integer
    except ValueError:
        return False
