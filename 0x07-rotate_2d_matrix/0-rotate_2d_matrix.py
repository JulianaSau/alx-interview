#!/usr/bin/python3
"""
Given an n x n matrix, rotate it 90 degrees clockwise
The matrix must be edited in-place
"""


def rotate_2d_matrix(matrix):
    """
    rotate the matrix clockwise (90 degrees)
    """
    zipped = zip(*reversed(matrix))
    for column1, column2 in enumerate(zipped):
        matrix[column1] = list(column2)
