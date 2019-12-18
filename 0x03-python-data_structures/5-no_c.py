#!/usr/bin/python3
def no_c(my_string):
    lists = list(my_string)
    [lists.remove(i) for i in lists if i == 'c' or i == 'C']
    return "".join(lists)
