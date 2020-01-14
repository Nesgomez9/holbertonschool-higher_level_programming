#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """ Class for unittest of max_integer function"""

    def test_max_intlist(self):
        """ Test list with intergers"""
        self.assertEqual(max_integer([10, 15, 58]), 58)

    def test_max_intlist_neg(self):
         """ Test list with intergers"""
        self.assertEqual(max_integer([-5, -15]), -5)

    def test_max_floatlist(self):
        """ Test when a list of floats is passed """
        self.assertEqual(max_integer([1.5, 4]), 4)

    def test_max_floatlist_neg(self):
        """ Test when a list of neg floats is passed """
        self.assertEqual(max_integer([-2.08, -3.2, -7.5, -10.0]), -2.08)

    def test_max_empty(self):
        """ Test when an empty list function is passed """
        self.assertEqual(max_integer([]), None)

    def test_max_repeatedint(self):
        """ Test when a single int is passed as list """
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_max_nolistint(self):
        """ Test when an integer is passed to function """
        with self.assertRaises(TypeError):
            max_integer(10)

    def test_max_char(self):
        """ Test when a list of chars is passed """
        self.assertEqual(max_integer(["1", "2", "a", "4"]), 'a')

    def test_max_liststromt(self):
        """ Test when a list with number and string is passed """
        with self.assertRaises(TypeError):
            max_integer([1, "Hola"])
