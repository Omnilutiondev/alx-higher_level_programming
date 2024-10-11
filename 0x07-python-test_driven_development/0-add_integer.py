#!/usr/bin/python3
"""TDD Module 0 for add_integer method."""


def add_integer(a, b=98):
    """Add the two integers.

    Args:
        a: is the first integer.
        b: is the second integer, default 98.

    Raises:
        TypeError: if a and/or b are not int, float.

    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
