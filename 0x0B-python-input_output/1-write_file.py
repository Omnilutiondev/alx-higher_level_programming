#!/usr/bin/python3
"""This function writes a string to a text file and returns the number of chars written"""

def write_file(filename="", text=""):
    """this appends the filename to the utf-8 encoding file set"""
    with open(filename, 'w', encoding="utf-8") as wtf:
        return wtf.write(text)
