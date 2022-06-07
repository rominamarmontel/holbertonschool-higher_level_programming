#!/usr/bin/python3
""" Module Square """
from ctypes import sizeof
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define Class Square
    inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of Square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Definition of method str
            Return: [Rectangle] (<id>) <x>/<y> - <size> """
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return "[Square] ({}) {}/{} - {}".format(i, x, y, s)

    @property
    def size(self):
        """ The public getter for public instance attribute size """
        return self.width

    @size.setter
    def size(self, value):
        """ The public setter for public instance attribute size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Definition of method update
            To assign an argument to each attribute """
        attr = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i != 4:
                    setattr(self, attr[i], arg)
        else:
            for key in kwargs:
                if key in attr:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Definition of method to_dictionary
            Returns: the dictionary representation of a Square """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
