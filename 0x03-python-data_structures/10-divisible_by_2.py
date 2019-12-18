#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i, count in enumerate(my_list):
        if count % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return (new)
