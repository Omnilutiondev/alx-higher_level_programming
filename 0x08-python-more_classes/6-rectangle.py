#!/usr/bin/python3
""" Class Rectangle create and decon """


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private inst attrib: width (int)
    Private inst attrib: height (int)
    Instantiation with varied width and height
    Public inst method: def area(self)
    Public inst method: def perimeter(self)
    print() and str() should print the rectangle using char #
    repr() should return a str representation of the rectangle
     to be able to recreate a new inst by using eval()
    deconstructor method implemented 'Bye rectangle...'
    Public class asttrib number_of_instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ The Constructor method """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """ Returns the area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Returns str to print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += '#'
            if col != self.height - 1:
                to_print += '\n'
        return to_print

    def __repr__(self):
        """ Returns a str representation of the rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ The Deconstructor method """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
