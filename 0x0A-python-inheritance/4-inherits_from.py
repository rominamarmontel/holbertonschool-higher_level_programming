#!/usr/bin/python3
"""
Define inherits_from
"""


def inherits_from(obj, a_class):
    a = type(obj)
    if a is not a_class:
        return issubclass(a, a_class)
    else:
        return False
