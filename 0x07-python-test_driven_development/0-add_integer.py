#!/bin/usr/python3

"""
Project of unitest

"""


def add_integer(a, b=98):

    """Function that adds 2 integers"""
    if isinstance(a, (int, float)) and type(a) != bool:
        if isinstance(b, (int, float)) and type(b) != bool:
            a = int(a)
            b = int(b)
            return(a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
