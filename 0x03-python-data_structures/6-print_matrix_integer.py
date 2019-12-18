#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    space = ""
    for i in matrix:
        for j in i:
            print("{:s}{:d}".format(space, j), end='')
            space = " "
        print("")
