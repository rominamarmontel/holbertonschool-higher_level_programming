#!/usr/bin/python3
"""
Define Rectangle Class
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
