#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    """ function that returns the JSON representation of an object"""
    with open(filename, "r", encoding="utf-8") as file1:
        return json.load(my_obj, file1)
