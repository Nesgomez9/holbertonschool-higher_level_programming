#!/usr/bin/python3
def number_of_lines(filename=""):
    """ This function reads the text of the file and returns the number
    of lines in it
    """
    with open(filename, "r", encoding="utf-8") as file1:
        return len(file1.readlines())
