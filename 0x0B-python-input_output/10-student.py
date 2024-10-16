#!/usr/bin/python3
"""This class defines a student based on 9-student.py"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """intialize the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dict representation of a student instance
        if attrs is a slist of strings, only attributed names are
        contained in this list must be retrieved.
        Otherwise, retrieve all attrs"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
