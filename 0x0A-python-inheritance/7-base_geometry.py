#!/usr/bin/python3
"""
Define class BaseGeometry
"""


class BaseGeometry:
    """ class BaseGeometry """
    def area(self):
        """ Area : Define Instance Method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Value : Define Instance Method """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif 0 >= value:
            raise ValueError("{:s} must be greater than 0".format(name))
