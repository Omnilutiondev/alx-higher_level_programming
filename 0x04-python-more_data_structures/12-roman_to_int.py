#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    totalstr = 0
    numstr = 0
    romdigits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for px in reversed(roman_string):
    numstr = romdigits[px]
    totalstr += numstr if totalstr < numstr * 5 else -numstr
    return total
