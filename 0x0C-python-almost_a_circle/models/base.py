#!/usr/bin/python3

import json

"""Module Base for REctangle and Square"""

class Base:
    """Base Clase"""
    __nb_objects = 0
    def __init__(self, id=None):
        """ Constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON string of a dictionary"""
        return json.dumps(list_dictionaries)
