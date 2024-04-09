#!/usr/bin/python3

"""creating a class"""


class Rectangle:
    """This class defines a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This function returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method that defines the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that returns the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
