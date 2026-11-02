#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    Return the perimeter of the island described in grid.
    grid is a list of lists of integers: 0 is water, 1 is land.
    Each land cell adds 4 sides, minus 2 for every pair of
    horizontally or vertically adjacent land cells.
    """
    perimeter = 0
    rows = len(grid)

    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i + 1 < rows and j < len(grid[i + 1]) \
                        and grid[i + 1][j] == 1:
                    perimeter -= 2
                if j + 1 < cols and grid[i][j + 1] == 1:
                    perimeter -= 2

    return perimeter
