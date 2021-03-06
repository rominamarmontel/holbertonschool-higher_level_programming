#!/usr/bin/python3
"""
    Module Rectangle
"""


class Rectangle:
    """
    Definition of a Class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        The instance method called when a new object is created
        Args:
            width : a private attribute
            height : a private attribute
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public Instance : Area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public Instance : Perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Instance Method : str
        """
        print_string = ""
        if self.__width == 0 or self.__height == 0:
            return print_string
        else:
            for x in range(0, self.__height):
                for y in range(0, self.__width):
                    print_string += "#"
                if x < self.__height - 1:
                    print_string += "\n"
            return print_string

    def __repr__(self):
        """
        Instance Method : repr
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
