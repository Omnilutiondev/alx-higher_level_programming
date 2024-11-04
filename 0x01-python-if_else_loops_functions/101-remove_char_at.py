#!/usr/bin/python3
def remove_char_at(str, n):
    newstrng = ""
    for idx, c in enumerate(str):
        if idx != n:
            newstrng += c
            return newstrng
