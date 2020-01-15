#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0

    """defines rectangle  """
    def __init__(self, width=0, height=0):
        """ init atributes"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    def perimeter(self):
        """ Method for perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def area(self):
        """Method to find the area"""
        return(self.width * self.height)

    def __str__(self):
        """Method to return a string"""
        square = ""
        if self.width == 0 or self.height == 0:
            return(square)
        for i in range(self.__height):
                square += str("#" * self.__width) + "\n"
        return square[:-1]

    def __repr__(self):
        """ Method returns Representation of a object like a string"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Bye rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
