#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests for the function max_integer
    """

    def test_empty_args(self):
        """ Test if list in arg is empty and return None """
        self.assertEqual(max_integer([]), None)

    def test_max_first(self):
        """ Test case if maximal value is the first"""
        self.assertEqual(max_integer([52, 25, 3, 18, 7]), 52)

    def test_max_middle(self):
        """ Test case if maximal value is in middle of list"""
        self.assertEqual(max_integer([2, 6, 84, 25, 12]), 84)

    def test_max_end(self):
        """ Test case if maximal value is the last element in list"""
        self.assertEqual(max_integer([3, 11, 7, 3, 28]), 28)

    def test_negativ_number(self):
        """ Test case if list contain negativ number"""
        self.assertEqual(max_integer([-12, 6, -3, 25, 16]), 25)

    def test_negativ_number(self):
        """ Test case if list contain only negativ number"""
        self.assertEqual(max_integer([-12, -6, -3, -25, -16]), -3)

    def test_one_single_element(self):
        """ Test case if list contain only one number"""
        self.assertEqual(max_integer([5]), 5)


if __name__ == '__main__':
    unittest.main()
