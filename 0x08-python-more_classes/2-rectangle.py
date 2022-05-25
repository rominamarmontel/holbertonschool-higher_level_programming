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
        """ The method : width
            Return : the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ The method : width
        Args:
            value : the width of rectangle (integer)
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ The method : height
            Return : the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ The Method : height
        Args:
            value : the height of rectangle (integer)
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ The public instance : area
            Return : the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ The public instance : perimeter
            Return : the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
