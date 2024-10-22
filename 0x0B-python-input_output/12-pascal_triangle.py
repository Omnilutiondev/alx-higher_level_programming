#!/usr/bin/python3
"""this function returns a list of lists of
integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """This defines the size of n in the triangle"""
    if n <= 0:
        return []

    ptriangle = [[1]]
    while len(ptriangle) != n:
        ptr = ptriangle[-1]
        temp = [1]
        for r in range(len(ptr) - 1):
            temp.append(ptr[r] + ptr[r + 1])
        temp.append(1)
        ptriangle.append(temp)
    return ptriangle
