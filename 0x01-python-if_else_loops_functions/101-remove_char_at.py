#!/usr/bin/python3
def remove_char_at(str, n):
    newstrng = ""
    for idx, cdx in enumerate(str):
        if idx != n:
            newstrng += cdx
            return newstrng
