#!/usr/bin/python3
""" Module with the Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter of the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of the height attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gettet of the X attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter of the x attribute """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter of the Y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter of the Y attribute """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method That returns the area of a Rectangle """
        return (self.width * self.height)

    def display(self):
        """ Method that display a representation of the Rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print("{:s}".format(' ' * self.x), end='')
            print("{:s}".format('#' * self.width))

    def __str__(self):
        """ str method that returns a string representation of a rectangle """
        s = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Method Updates that updates an attribute of a Rectangle """
        count = 0
        attr = ["id", "width", "height", "x", "y"]

        for arg in args:
            if not count:
                super().__init__(arg)
            else:
                setattr(self, attr[count], arg)
            count += 1

        if not args or not len(args):
            for key in kwargs:
                if key == "id":
                    super().__init__(kwargs[key])
                else:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Returns dictionary representation of a Rectangle """
        dic = {"id": self.id, "width": self.width, "height": self.height,
               "x": self.x, "y": self.y}
        return dic
