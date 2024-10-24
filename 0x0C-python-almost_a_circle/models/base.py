#!/usr/bin/python3
"""This function is for creating the first base class"""


class Base:
    """This represents the base of the OOP hierarchy to be used"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this is the constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
