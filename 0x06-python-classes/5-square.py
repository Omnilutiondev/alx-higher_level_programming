#!/usr/bin/python3
"""The Square module."""


class Square:
    """This defines a square."""

    def __init__(self, size=0):
        """The main constructor.

        Args:
            size: The length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """The property for the length of a side of this square.

        Raise:
            TypeError: If the instance size is not an integer
            ValueError: If the instance size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """The Area of this square,

        Return:
        The size squared.
        """
        return self.__size ** 2

    def my_print(self):
        """This prints this square."""
        for idx in range(self.size):
            for jdx in range(self.size):
                print("#", end="\n" if jdx is self.size and idx != jdx else "")
        print()

