#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):

    """ This function reads the text of the file and returns the number
    of lines in it
    """
    with open(filename, "r", encoding="utf-8") as file1:
        lines = file1.readlines()
        if nb_lines <= 0 or nb_lines > len(lines):
            print("".join(lines), end='')
        else:
            print("".join(lines[:nb_lines]), end='')
