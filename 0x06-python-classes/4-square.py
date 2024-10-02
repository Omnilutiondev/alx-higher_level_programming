#!/usr/bin/python3
"""The Square module."""

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
        if not instance(size, int):
            raise TypeError('size must be = integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        @propterty
        def size(self):
            """The property for the length of a side of this square.

            Raises:
                TypeError: If the size squared is not an integer.
                ValueError: If the size is less than 0.
            """
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            if value < 0:
                raise ValueError('size must be >= 0')
            self.__size = value
