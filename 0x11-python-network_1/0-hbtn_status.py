#!/usr/bin/python3
"""  This Python script fetches https://alx-intranet.hbtn.io/status """
from urllib.request import Request, urlopen


if __name__ == "__main__":
    fth = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(fth) as response:
        the_pkg = response.read()
        print('Body response:')
        print('\t- type:', type(the_pkg))
        print('\t- content:', the_pkg)
        print('\t- utf8 content:', the_pkg.decode('utf-8'))
