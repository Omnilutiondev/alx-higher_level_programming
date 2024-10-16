#!/usr/bin/python3
"""This function that creates an
Object from a Json file"""


import json


def load_from_json_file(filename):
    """create an object from a json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
