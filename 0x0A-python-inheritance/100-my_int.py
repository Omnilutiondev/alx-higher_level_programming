#!/usr/bin/python3
"""
Inherit the class MyInt
"""


class MyInt(int):
    """change an integer, perfect for opposite!"""
    def __new__(cls, *args, **kwargs):
        """add a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """swap != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """swap == is now !="""
        return int(self) == other
