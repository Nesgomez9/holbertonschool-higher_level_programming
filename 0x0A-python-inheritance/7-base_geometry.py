#!/usr/bin/python3


class BaseGeometry:
    """ Geometry Class """
    def area(self):
        """ Method not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is a number greater than 0"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
