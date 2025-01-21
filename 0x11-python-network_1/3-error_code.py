#!/usr/bin/python3
""" This Python script takes in a URL,
sends a request to it
and displays the body of the response
(decoded in utf-8)
"""
import sys
from urllib.request import Request, urlopen
import urllib.error


if __name__ == "__main__":
    web = sys.argv[1]

    fth = Request(web)
    try:
        with urlopen(fth) as response:
            the_pkg = response.read().decode('utf-8')
            print(the_pkg)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
