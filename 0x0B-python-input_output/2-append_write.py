#!/usr/bin/python3
"""
Define the append_write function
"""


def append_write(filename="", text=""):
    """ The function appends a string at the end of a text file
    and returns the number of characters added """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
