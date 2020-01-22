#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    """ function that returns the JSON representation of an object"""
    with open(filename, "w") as file1:
        json.dump(my_obj, file1)
