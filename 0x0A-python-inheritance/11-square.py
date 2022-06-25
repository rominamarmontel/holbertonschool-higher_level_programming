#!/usr/bin/python3
"""
Define class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square inherits from Rectangle"""
    def __init__(self, size):
        """ Initialize square constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area : return the area of square """
        return self.__size ** 2

    def __str__(self):
        """ Str : Square description """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
