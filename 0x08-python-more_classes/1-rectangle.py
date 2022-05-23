#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """ Definition of a Class Rectangle

    """
    def __init__(self, width=0, height=0):       
        self.height = height
        self.width = width
        
        @property
        def height(self):
            return self.__height
            """ The method : height
            Return : the height of rectangle
            """

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

        @property
        def width(self):
            return self.__width
            """ The method : width
            Return : the width of rectangle
            """

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