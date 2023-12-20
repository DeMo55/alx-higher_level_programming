#!/usr/bin/python3
"""
Module 3-square.py.

This module has only one class.

Classes:
    Square:
        A class representing a Square.

Functions:
    This module has no functions.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int) : Private instance attribute.
            The size of a new square object.

    Methods:
        __init__(self, size=0) :
            Initializes a new square object with the given attribute.

        area(self) :
            Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square object with the given attribute.

        Args:
            size (int) : Private instance attribute.
                The size of a new square object. The default value = 0.

        Raises:
            TypError:
                If `size` is not an integer.
            ValueError:
                If `size` is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the current square area.

        Args:
            This method takes no arguments.

        Returns:
            square_area (int) :
                The area of the square based on the value of `size `.
        """
        square_area = self.__size ** 2
        return square_area
