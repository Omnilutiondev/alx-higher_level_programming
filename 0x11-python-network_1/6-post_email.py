#!/usr/bin/python3
""" This Python script takes in a URL and an email address,
sends a POST request to it with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    web = sys.argv[1]
    email = {'email': sys.argv[2]}
    c = requests.post(web, data=email)
    print(c.text)
