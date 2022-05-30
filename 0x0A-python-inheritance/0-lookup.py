#!/usr/bin/python3
"""
The lookup function that returns a list of
available attributes and methods of an objec
"""


def lookup(obj):
    """lookup returns a list of available
    attributes and methods of an object"""
    return dir(obj)
