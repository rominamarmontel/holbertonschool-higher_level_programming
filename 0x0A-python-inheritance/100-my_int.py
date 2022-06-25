#!/usr/bin/python3
"""
Define class MyInt
"""


class MyInt(int):
    """
    Class MyInt
    """
    def __init__(self, int):
        """instance method create an object"""
        self.__int = int

    def __ne__(self, int):
        """instance method return equal value"""
        return self.__int == self.__int

    def __eq__(self, int):
        """instance method return no-equal value"""
        return self.__int != self.__int
