#!/usr/bin/python3
""" This Python script fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    c = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(c.text))
    print('\t- content:', c.text)
