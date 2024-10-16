#!/usr/bin/python3
"""This class represents a student"""


class Student:
    """Representation of a new student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary that is a rep of a student instance"""
        return self.__dict__
