#!/usr/bin/python3
"""
Module 4-square.py.

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

        size(self) : @property
            Gets the property `size`.

        size(self, value) : @size.setter
            Sets the property `size`.

        area(self) :
            Returns the current square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new square object with the given attribute.

        Args:
            size (int) : Private instance attribute.
                The size of a new square object. The default value = 0.

        """
        self.size = size

    @property
    def size(self):
        """
        This method gets the property `size`.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the property `size`.

        Args:
            value (int): Private instance attribute.
                The size of a new square object.

        Raises:
            TypError:
                If `value` is not an integer.
            ValueError:
                If `value` is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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
