#!/usr/bin/python3
"""
Define is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
