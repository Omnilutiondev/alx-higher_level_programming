#!/usr/bin/python3
"""The Define a class Square module."""

class Square:
    """This represents a square."""

    def init(self, size=0, position=(0, 0)):
        """This initializes a new square.

        Args:
            size (int): The length of a side of the square.
            position (int, int): The position of the new square created/
        """
        self.__size = size
        self.position = position

    @property
    def size(self):                                                                                """Get or set the present size of this square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def size(self):
        """Get or set the present size of this square."""
        return (self.__size)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
        
    def area(self):
        """Return the size current area of the square in question."""
        return (self.__size * self.__size)

    def my_print(self):
        """This prints this square using #."""
        if self.__size == 0:
            print("")
            return
        
        [print("") for idx in range(0, self.__position[1])]
        print()
