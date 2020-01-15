#!/usr/bin/python3
class Square:

    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Constructor"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' Return the area of the instance square'''
        return self.__size ** 2