#!/usr/bin/python3
"""
    Generate Pascal's triangle up to n rows.
    """
def pascal_triangle(n):
    '''
    Generate Pascal's triangle up to n rows.

    In Pascal's triangle, each number is the sum of the two numbers directly above it.

    Parameters:
    n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    list of lists of int: A list of lists of integers representing Pascal's triangle.
    '''
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle