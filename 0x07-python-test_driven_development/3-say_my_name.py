#!/usr/bin/python3
"""
The My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function: say_my_name
        prints My name is <first name> <last name>
    @first_name: must be a list of lists of integers or floats
    @last_name: must be a number (integer or float)
    Return: None
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
