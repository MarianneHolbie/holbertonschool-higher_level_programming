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
    len_row = len(matrix[0])
    len_column = len(matrix[1])

    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if len_row != len_column:
        raise TypeError('Each row of the matrix must have the same size')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        new_value = []
        for element in row:
            new_value.append(round(element/div, 2))
        new_matrix.append(new_value)
    return (new_matrix)
