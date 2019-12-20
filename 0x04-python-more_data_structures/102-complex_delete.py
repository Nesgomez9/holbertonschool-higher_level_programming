#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listd = list(a_dictionary.keys())
    for i in listd:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
