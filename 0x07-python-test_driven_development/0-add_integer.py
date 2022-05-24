#!/usr/bin/python3
"""
The division module that add deux elements.
"""


def add_integer(a, b=98):
    """
    Function: add_integer(a, b=98)
        an addition a and b
    @a: integer
    @b: integer
    Return: the add of a and b, an exact integer
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
