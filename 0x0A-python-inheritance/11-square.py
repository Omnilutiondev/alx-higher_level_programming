#!/usr/bin/python3
'''Function for Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass for a rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Parameter for area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''Return string of this square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
