#!/usr/bin/python3
""" Contains a class to create a square """


class Square():
    """ Initialize these attributes to 0 """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Set square attributes """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of a Square """
        return (self.width + self.height) * 2

    def __str__(self):
        """ String version of a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square if this file was executed """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
