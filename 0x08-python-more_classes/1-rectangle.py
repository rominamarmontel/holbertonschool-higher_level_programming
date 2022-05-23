#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """ Definition of a Class Rectangle

    """
    def __init__(self, width=0, height=0):
        """ Init a rectangle 
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.height = height
        self.width = width
        
    @property
    def width(self):
        """ The method : width
        Return : the width of rectangle
        """
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
        self.__width = value
        
    @property
    def height(self):
        """ The method : height
        Return : the height of rectangle
        """
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
        self.__height = value
