#!/usr/bin/python3
"""
The division module that divides all elements of matrix
"""


def matrix_divided(matrix, div):
    """
    Function: matrix_divided(matrix, div)
        The division module divides all elements of matrix
    @matrix: must be a list of lists of integers or floats
    @div: must be a number (integer or float)
    Return: a new matrix
    """

    new = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
        (list of lists) of integers/floats")
    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif type(div) == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i in range(0, 2):
            new.append(list(map(lambda x: round(x / div, 2), matrix[i])))
        return new
