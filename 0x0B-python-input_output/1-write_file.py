#!/usr/bin/python3
"""
Define the write_file function
"""


def write_file(filename="", text=""):
    """ The function writes a string to a text file
    and returns the number of characters written """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
