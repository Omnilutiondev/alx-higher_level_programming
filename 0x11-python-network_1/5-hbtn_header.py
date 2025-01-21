#!/usr/bin/python3
""" This Python script takes in a URL,
sends a request to it and displays
the value of the variable X-Request-Id
in the response header """
import sys
import requests


if __name__ == "__main__":
    web = sys.argv[1]

    c = requests.get(web)
    print(c.headers.get("X-Request-Id"))
