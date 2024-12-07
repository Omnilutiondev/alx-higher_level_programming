#!/usr/bin/python3
'''Function for lookup method.'''


def lookup(obj):
    '''Looks for the object attributes and methods.
    Args:
        obj (object): the object to the list.

    Returns:
        list: the list of all attributes.
    '''
    return dir(obj)
