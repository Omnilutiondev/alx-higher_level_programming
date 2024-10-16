#!/usr/bin/python3
"""this function returns an object
represented by a JSON string"""


import json


def from_json_string(my_str):
    """return the json string"""
    return json.loads(my_str)

