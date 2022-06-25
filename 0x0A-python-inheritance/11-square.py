#!/usr/bin/python3
"""
Define class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGeometory"""
    def __init__(self, width, height):
        """ Initialize rectangle constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Area : Define Instance Method """
        return self.__width * self.__height

    def __str__(self):
        """ Str : Rectangle description """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


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
