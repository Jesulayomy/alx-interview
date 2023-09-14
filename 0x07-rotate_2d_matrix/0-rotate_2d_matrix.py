#!/usr/bin/python3
""" Documentation for the Interview question """


def rotate_2d_matrix(matrix):
    """ Rotato a two dimensional matrix 90 deg clockwise """
    size = len(matrix)
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[size - 1 - j][i]
            matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
            matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
            matrix[j][size - 1 - i] = temp
