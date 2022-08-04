#!/usr/bin/python3
"""A python class for a square
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square()
    Args:
        Rectangle (class): inheriting the rectangle class
    """

    def __init__(self, size):
        """Square(size)
        Args:
            size (int): the size of the sides of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """area() returns the area of the square
        """
        return self.__size ** 2
