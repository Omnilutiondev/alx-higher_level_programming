#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for px in sorted(a_dictionary.keys()):
        print("{}: {}".format(px, a_dictionary[px]))
