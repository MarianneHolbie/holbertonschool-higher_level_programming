#!/usr/bin/python3
"""
MODULE MATRIW DIVIDED

-----------------------------------------------------------------------
FUNCTION(S)

        matrix_divided : function that divide given matrix by given number

-----------------------------------------------------------------------

"""


def matrix_divided(matrix, div):
    """
    Function that divide given matrix by given number div

    Args :
        matrix : matrix of values
        div: number use to divise each element of the matrix

    Return:
        new matrix
        each value rounded to 2 decomal places

    Raises:
        Test TypeError and ZeroDivisionError


    """

    new_matrix = []
    len_matrix = len(matrix[0])

    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        new_value = []
        len_row = len(row)
        if len_matrix != len_row:
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if isinstance(element, (int, float)):
                new_value.append(round(element/div, 2))
            else:
                raise TypeError(
                    "matrix must be a matrix(list"
                    "of lists) of integers/floats")
        new_matrix.append(new_value)
    return (new_matrix)
