#!/usr/bin/python3
"""The Square module."""


class Square:
    """This defines a square."""

    def __init__(self, size=0):
        """The main constructor.

        Args:
            size: The length of a side of the square.

        Raise:
            TypeError: If the instance size is not an integer
            ValueError: If the instance size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """The Area of this square.

        Return:
            The size squared.
        """
        return self.__size ** 2
