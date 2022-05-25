#!/usr/bin/python3
"""
The function that prints a square with the character #
"""


def print_square(size):
    """
    Function: print_square
        prints a square with the character #
    @size: length of the square
    Return: None
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(0, size):
            for column in range(0, size):
                print("#", end="")
            print()
