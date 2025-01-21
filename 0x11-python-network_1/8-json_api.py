#!/usr/bin/python3
""" This Python script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        let = ""
    else:
        let = sys.argv[1]
    q_data = {"q": let}

    c = requests.post('http://0.0.0.0:5000/search_user', data=q_data)
    try:
        response = c.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
