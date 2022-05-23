#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """ Definition of a Class Rectangle

    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            """initializes the Rectangle
            Args:
                width : integer
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """initializes the Rectangle
            Args:
                height : integer
            """
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
