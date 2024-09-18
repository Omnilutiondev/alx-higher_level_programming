#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keyy in list(a_dictionary.keys()):
        if a_dictionary[keyy] == value:
            del a_dictionary[keyy]
            return a_dictionary
