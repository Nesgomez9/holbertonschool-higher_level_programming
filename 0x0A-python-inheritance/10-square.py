#!/usr/bin/python3

""" Class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square"""

    def __init__(self, size):
        """ Constructor of the Square Class """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
