#!/usr/bin/python3

""" class that inherits from  int """


class MyInt(int):
    def __eq__(self, value):
        return int(self) != value

    def __ne__(self, value):
        return int(self) == value
