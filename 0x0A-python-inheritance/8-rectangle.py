#!/usr/bin/python3

""" Class that inherits from base Geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to define object Rectangle"""

    def __init__(self, width, height):
        """ Constructor of the class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
