#!/usr/bin/python3
"""This function writes an object
to a text file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, 'z', encoding="utf-8") as f:
        json.dump(my_obj, f)
