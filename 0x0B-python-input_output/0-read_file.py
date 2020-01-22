#!/usr/bin/python3
def read_file(filename=""):
    """ This function reads the text of the file """

    with open(filename, "r", encoding="utf-8") as file1:
        print(file1.read(), end='')
