#!/usr/bin/python3
"""this function returns a list of lists of
integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """This defines the size of n in the triangle"""
    if n <= 0:
        return []

    ptriangle = ([1])
    while len(ptriangle) != n:
        ptr = ptriangle[-1]
        temp = [1]
        for t in range(len(ptr) - 1):
            temp.append(ptr[t] + ptr[t + 1])
        temp.append(1)
        ptriangle.append(temp)
    return ptriangle
