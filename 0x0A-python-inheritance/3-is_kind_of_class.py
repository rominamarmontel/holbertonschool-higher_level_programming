#!/usr/bin/python3
"""
Define is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is
    exactly an instance of the specified class """
    if isinstance(obj, a_class):
        return True
    return False
