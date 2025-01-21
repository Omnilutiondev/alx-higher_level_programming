#!/usr/bin/python3
""" This Python script takes in a URL,
sends a request to it
and displays the body of the response."""
import sys
import requests


if __name__ == "__main__":
    web = sys.argv[1]
    c = requests.get(web)
    if c.status_code >= 400:
        print('Error code:', c.status_code)
    else:
        print(c.text)
