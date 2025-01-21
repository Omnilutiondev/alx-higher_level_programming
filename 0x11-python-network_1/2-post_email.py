#!/usr/bin/python3
""" This Python script takes in a
URL and an email,
sends a POST request to it
with the email as a parameter,
and displays the body of the response
(encoded in utf-8)
"""
from urllib.request import Request, urlopen
import urllib.parse
import sys


if __name__ == "__main__":
    web = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    fth = Request(web, data)
    with urlopen(fth) as response:
        the_pkg = response.read().decode('utf-8')
        print(the_pkg)
