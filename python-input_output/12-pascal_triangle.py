#!/bin/usr/python3
"""
    Function create Pascal's Triangle
"""


def pascal_triangle(n):
    """
        give the result of (a+b)^n for all n
    """

    if n <= 0:
        return ([])
    # base case
    elif n == 1:
        return ([[1]])
    else:
        # each line begin by 1
        new_line = [1]
        # recursiv call of function
        result = pascal_triangle(n - 1)
        last_line = result[-1]
        # use previous line to calculate current line
        for i in range(len(last_line) - 1):
            # sum of the 2 entries directly above
            new_line.append(last_line[i] + last_line[i + 1])
        # every line finish by 1
        new_line += [1]
        result.append(new_line)
        return (result)
