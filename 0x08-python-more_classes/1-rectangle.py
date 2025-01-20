#!/usr/bin/python3
""" Class Rectangle with h x w """


class Rectangle:
    """
    Class that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with an varied width and heigh
    """

    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the width property """
        return self.__width

    @property
    def height(self):
        """ gets the height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets the width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
