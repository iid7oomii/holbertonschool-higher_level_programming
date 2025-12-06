#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Returns a new matrix with results rounded to 2 decimal places.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"
    msg_div = "div must be a number"
    msg_zero = "division by zero"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_type)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg_type)

    len_rows = len(matrix[0])
    for row in matrix:
        if len(row) != len_rows:
            raise TypeError(msg_size)

    if not isinstance(div, (int, float)):
        raise TypeError(msg_div)

    if div == 0:
        raise ZeroDivisionError(msg_zero)

    return [[round(x / div, 2) for x in row] for row in matrix]
