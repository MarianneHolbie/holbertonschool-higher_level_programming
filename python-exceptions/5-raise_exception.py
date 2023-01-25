#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Exception has been raised")
    except TypeError as te:
        print(te)
