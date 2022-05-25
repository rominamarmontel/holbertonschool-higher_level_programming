#!/usr/bin/python3
"""
A class Square that defines a square

"""


class Square:
    """Definition of a Class Square"""

    def __init__(self, size=0):
        """
        initialize square attributes

        Attributes: size (int)
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    def size(self):
        return self.__size

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
