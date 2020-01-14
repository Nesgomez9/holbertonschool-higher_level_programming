#!/bin/usr/python3

"""Project to learn unitest"""


def print_square(size):

    """Function that prints a square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for c in range(size):
        print('#' * size)
