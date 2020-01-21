#!/usr/bin/python3

""" Class that inherits from base Geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to define a Rectangle"""

    def __init__(self, width, height):
        """ Constructor of the Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method for the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Method for print that returns a string"""
        string = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return string
