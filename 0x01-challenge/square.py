#!/usr/bin/python3
"""Contains a Sqaure"""


class Rectangle():
    """ Now it is Rectangle. :)"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_Rectangle(self):
        """ Area of the Rectangle """
        return self.width * self.height

    def permiter_of_my_Rectangle(self):
        """ Perimeter of the Rectangle"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Rectangle(width=12, height=9)
    print(s)
    print(s.area_of_my_Rectangle())
    print(s.permiter_of_my_Rectangle())
