#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(reponese.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))