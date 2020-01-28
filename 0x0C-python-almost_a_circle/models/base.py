#!/usr/bin/python3
"""Module Base for Rectangle and Square"""
import json
import csv


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
        """ Method that save the representation ob a object in a json into
        a file """
        obj_list = []
        if list_objs:
            for i in list_objs:
                obj_list.append(i.to_dictionary())
        s = cls.to_json_string(obj_list)
        with open("%s.json" % cls.__name__, "w", encoding="utf-8") as file1:
            file1.write(s)

    @staticmethod
    def from_json_string(json_string):
        """ Convert a JSON string into a python dictionary """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a new instance with the attributes that are defines
        the dictionary """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        elif cls.__name__ == "Square":
            dummy = cls(10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Return a list of instance of a file"""
        try:
            with open("%s.json" % cls.__name__, encoding="utf-8") as file1:
                r = file1.read()
                dic = cls.from_json_string(r)
                list1 = []
                for i in dic:
                    list1.append(cls.create(**i))
                return list1
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes"""
        with open("%s.csv" % cls.__name__, 'w', newline='') as cf:
            wr = csv.writer(cf)
            if cls.__name__ is "Square":
                for i in list_objs:
                    wr.writerow([i.id, i.size, i.x, i.y])
            elif cls.__name__ is "Rectangle":
                for i in list_objs:
                    wr.writerow([i.id, i.width, i.height, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes"""
        rlist = []
        try:
            with open("%s.csv" % cls.__name__, 'r') as cf:
                rd = csv.reader(cf)
                for i in rd:
                    if cls.__name__ is "Square":
                        dic1 = {"id": int(i[0]), "size": int(i[1]),
                                "x": int(i[2]), "y": int(i[3])}
                    elif cls.__name__ is "Rectangle":
                        dic1 = {"id": int(i[0]), "width": int(i[1]),
                                "height": int(i[2]), "x": int(i[3]),
                                "y": int(i[4])}
                    rlist.append(cls.create(**dic1))
            return rlist
        except:
            return []
