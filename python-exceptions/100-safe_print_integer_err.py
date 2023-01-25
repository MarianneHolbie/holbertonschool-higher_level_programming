#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))

    except ValueError as ve:
        print("Exception: {}".format(ve))
        return False
    except TypeError as te:
        print("Exception: {}".format(te))
        return False
    else:
        return True
