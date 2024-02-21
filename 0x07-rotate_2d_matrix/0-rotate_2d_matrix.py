#!/usr/bin/python3
'''rotate an n x n 2D matrix 90 degrees clockwise'''


def rotate_2d_matrix(matrix):
    '''Rotate 2D Matrix
    '''
    n = len(matrix)

    rotated_m = [['' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_m[j][n - i - 1] = matrix[i][j]

    matrix.clear()
    matrix.extend(rotated_m)
