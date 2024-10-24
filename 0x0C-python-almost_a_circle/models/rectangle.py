#!/usr/bin/pytho3
"""This is a class rectangle that inherits from Base"""
from models.base import Base


class Rectangle{Base}:
    """The rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width of the triangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """The height of the triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """The x coordinate of the triangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """The y coordinate of the triangle"""
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value
