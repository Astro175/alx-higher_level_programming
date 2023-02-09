#!/usr/bin/python3
"""
  Module that divides a matrix
"""


def matrix_divided(matrix, div):
    """
      Function that divides a matrix of lists
    """
    if type(matrix) != list or not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    if not all(isinstance(j, (int, float)) for i in matrix for j in i):
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(j / div, 2) for j in i] for i in matrix]
