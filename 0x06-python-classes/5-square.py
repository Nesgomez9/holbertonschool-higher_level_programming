#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
            self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        ''' Prints in stdout the square with the char #
        '''
        for i in range(self.__size):
            print("{:s}".format('#' * self.__size))
        if self.__size == 0:
            print("")
