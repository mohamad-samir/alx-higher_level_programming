#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n: int):
    """Returns a list of lists of numbers representing the Pascal's triangle.

    Args:
        n (int): Number of rows.

    Return:
        list of lists of numbers
        otherwise [] if n <= 0
    """
    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i-1][j-1] + result[i-1][j])
        row.append(1)
        result.append(row)

    return result
