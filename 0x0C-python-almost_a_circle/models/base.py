#!/usr/bin/python3
"""Module Base for Rectangle and Square"""
import json


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
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        obj_list = []
        if list_objs:
            for i in list_objs:
                obj_list.append(i.to_dictionary())
        s = cls.to_json_string(obj_list)
        with open("%s.json" % cls.__name__, "w", encoding="utf-8") as file1:
            file1.write(s)
