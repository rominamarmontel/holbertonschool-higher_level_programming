#!/usr/bin/python3
"""the function add_attribute"""


def add_attribute(obj, name, value):
    """function that adds a new attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
