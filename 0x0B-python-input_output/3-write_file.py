#!/usr/bin/python3
def write_file(filename="", text=""):

    """ This function reads the text of the file and write a string in it
    """
    with open(filename, "w", encoding="utf-8") as file1:
        return file1.write(text)
