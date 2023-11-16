#!/usr/bin/python3
"""_summary_
"""


def transpose_matrix(matrix, n):
    """ Transpose a matrix"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_matrix(matrix):
    """ Reverse a matrix """
    for row in matrix:
        row.reverse()

def rotate_2d_matrix(matrix):
    """ Rotate the 2d matrix"""
    n = len(matrix)
    print(n)
    transpose_matrix(matrix, n)
    reverse_matrix(matrix)
    return matrix
    