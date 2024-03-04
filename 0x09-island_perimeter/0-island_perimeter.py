#!/usr/bin/python3
'''Island Perimeter'''


def island_perimeter(grid):
    ''''''
    perimeter = 0
    for i, cell in enumerate(grid):
        for j, n in enumerate(cell):
            if n == 1:
                if cell[j - 1] == 0:
                    perimeter += 1
                if cell[j + 1] == 0:
                    perimeter += 1
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter
