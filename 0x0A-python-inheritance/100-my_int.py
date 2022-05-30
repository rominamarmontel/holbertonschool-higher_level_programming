#!/usr/bin/python3
"""
Define the MyInt class
"""


class MyInt(int):
    """ Inherit from int """
    def __eq__(self, other):
        """Equal to returns not equal to."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal to returns equal to."""
        return super().__eq__(other)
