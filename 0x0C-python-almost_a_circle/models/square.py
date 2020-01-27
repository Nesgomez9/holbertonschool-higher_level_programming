#!/usr/bin/python3
"""Module that contains the Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class that defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size,size,x,y,id)

    @property
    def size(self):
        """Size geter"""
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """ Method that returns the string representation of a Square"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Method that update an attribute of the object Square"""
        count = 0
        attr = ["id","size", "x", "y"]

        for arg in args:
            if not count:
                super().update(arg)
            else:
                setattr(self, attr[count], arg)
            count += 1

        if not args or not len(args):
            for key in kwargs:
                if key == "id":
                    super().update(kwargs[key])
                else:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Returns dictionary representation of a Rectangle """
        recdic = {"id": self.id,  "size": self.size,
                  "x": self.x, "y": self.y}
        return recdic
