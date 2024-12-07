#!/usr/bin/python3
'''The func BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Parameters to compute this area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Parameters for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
