#!/usr/bin/python3
"""
Define inherits_from
"""


def inherits_from(obj, a_class):
    """ function that returns True if the object
    is an instance of a class that inherited
    (directly or indirectly) from the specified class """
    if type(obj) is not a_class:
        return issubclass(obj, a_class)
    return False
