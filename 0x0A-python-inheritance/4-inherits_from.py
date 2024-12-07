#!/usr/bin/python3
'''The module is for inherits_from method.'''


def inherits_from(obj, a_class):
    '''Determine if an object is a true subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
