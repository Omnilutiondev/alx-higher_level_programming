#!/usr/bin/python3
"""The Square Module."""


class Square:
    """This defines a square."""

    def __init__(self, size):
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
