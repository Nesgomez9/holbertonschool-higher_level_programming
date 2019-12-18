#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if len(my_list) == 0:
        return (None)
    max = sorted(my_list)[-1]
    return (max)
