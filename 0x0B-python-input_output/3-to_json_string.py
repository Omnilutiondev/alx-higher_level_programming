#!/usr/bin/python3
"""This function that returns the JSON representation
of an object string"""


import json


def to_json_string(my_obj):
    """return json represtation of an object"""
    return json.dumps(my_obj)
