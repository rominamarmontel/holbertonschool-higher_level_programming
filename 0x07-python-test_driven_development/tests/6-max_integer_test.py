#!/usr/bin/python3
"""Module to find the max integer in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class of max_integer_tes.py
    """
    def test_max_integer(self):
        """test method for integers, strings
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 1, 2, -3]), 2)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0.1, 0.2, 0.3, 0.4]), 0.4)
        self.assertEqual(max_integer([-0.1, -0.2]), -0.1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer(['w', 'e', 'l', 'c']), 'w')
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
