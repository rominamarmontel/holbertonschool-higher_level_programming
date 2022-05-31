#!/usr/bin/python3
"""
Define the read_file function
"""


def read_file(filename=""):
    """ The function reads a text file and prints """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
