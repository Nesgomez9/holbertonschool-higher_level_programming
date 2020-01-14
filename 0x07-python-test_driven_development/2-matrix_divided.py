#!/bin/usr/python3

""" Project to estudy unitest"""


def matrix_divided(matrix, div):

    """Function that divide 2 Matrix"""

    if not isinstance(matrix, list) or \
       not all(isinstance(y, list) for y in matrix) or \
       not all([isinstance(x, (int, float)) for x in y] for y in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(y) == len(matrix[0]) for y in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)) or type(div) == bool:
        raise TypeError("div must be a number")
    new_matrix = [[round(a / div, 2) for a in b] for b in matrix]
    return new_matrix
