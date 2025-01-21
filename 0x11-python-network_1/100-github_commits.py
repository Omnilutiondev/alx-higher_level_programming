#!/usr/bin/python3
"""This script takes 2 args in order to list 10 commits
from the oldest to the newest one per line
"""
import requests
import sys


if __name__ == "__main__":
    web = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    c = requests.get(web)
    commits = c.json()
    try:
        for idx in range(10):
            print("{}: {}".format(
                commits[idx].get("sha"),
                commits[idx].get("commit").get("author").get("name")))
    except IndexError:
        pass
