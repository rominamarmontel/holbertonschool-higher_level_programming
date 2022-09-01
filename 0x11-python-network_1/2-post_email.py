#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')

    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
