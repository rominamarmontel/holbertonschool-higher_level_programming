#!/usr/bin/python3
"""
Function that adds 
a new attribute to an object
"""
def add_attribute(object, name, value):
    """ adds a new attribute to an object """
    if not hasattr(object,'__dict__'):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
