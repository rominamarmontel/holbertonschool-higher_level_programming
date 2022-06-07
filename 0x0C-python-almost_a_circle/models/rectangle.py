#!/usr/bin/python3
""" Module Rectangle """
from curses import keyname
from sys import argv
from models.base import Base


class Rectangle(Base):
    """ Define Class Rectangle
    inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor of Rectangle class """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("y must be an integer")
        elif x < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """ The public getter for private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ The public setter for private instance attribute width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ The public getter for private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ The public setter for private instance attribute height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ The public getter for private instance attribute x """
        return self.__x

    @x.setter
    def x(self, value):
        """ The public setter for private instance attribute x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ The public getter for private instance attribute y """
        return self.__y

    @y.setter
    def y(self, value):
        """ The public setter for private instance attribute y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Definition of method area
            Return: area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ Definition of method display
            Prints in stdout the Rectangle instance
            with the character # """
        print_string = ""
        if self.__width == 0 or self.__height == 0:
            return print_string
        else:
            for y in range(self.__y):
                print(" ")
            for height in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for width in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """ Definition of method str
            Return: [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """ Definition of method update
            To assign an argument to each attribute """
        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i != 5:
                    setattr(self, attr[i], arg)
        else:
            for key in kwargs:
                if key in attr:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Definition of method to_dictionary
            Returns: the dictionary representation of a Rectangle """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
