#!/usr/bin/python3
"""function that reads a text file"""

def read_file(filename=""):
    """reads the filename with utf-8 encoding"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
