#!/usr/bin/python3
''' Pascal's Triangle '''


def pascal_triangle(n):
    ''''''
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        temp = [0] + triangle[i] + [0]
        row = []

        for j in range(len(triangle[-1]) + 1):
            row.append(temp[j] + temp[j + 1])

        triangle.append(row)

    return triangle
