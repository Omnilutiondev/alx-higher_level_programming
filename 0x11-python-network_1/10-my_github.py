#!/usr/bin/python3
""" This Python script takes your GitHub credentials
and uses the GitHub API to display your id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    c = requests.get("https://api.github.com/user", auth=auth)
    print(c.json().get("id"))
