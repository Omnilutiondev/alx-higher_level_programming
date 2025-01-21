#!/usr/bin/python3
"""This Python script takes in a URL, sends a request to it and
displays the value of the X-Request-Id
variable found in the header of the response.
"""
import sys
from urllib.request import Request, urlopen


if __name__ == "__main__":
    cmd_url = sys.argv[1]
    fth = Request(cmd_url)
    with urlopen(fth) as response:
        print(dict(response.headers).get('X-Request-Id'))
