#!/usr/bin/python3
"""Python class module for a rectangle"
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    Args:
        BaseGeometry (class): inheriting from the BaseGeometry class
    """

    def __init__(self, width, height):

        """Rectangle(width, height)
        Args:
        -width: width property of the rectangle
        -height: height property of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
