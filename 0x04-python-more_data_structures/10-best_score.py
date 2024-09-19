#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxscor = 0
    maxkeyy = None
    for px, pv in a_dictionary.items():
        if pv > maxscor:
            maxscor = pv
            maxkeyy = px
        return maxkeyy
