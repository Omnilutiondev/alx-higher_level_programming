#!/usr/bin/python3
"""This function appends a str at the end of a text file
& returns the number of chars added"""


def append_write(filename="", text=""):
    """this appends the filename with the utf-8 encoding"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
