#!/usr/bin/python3
"""
Module 1-square.py.

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
        __init__(self, size) :
            Initializes a new square object with the given attribute.
    """

    def __init__(self, size):
        """
        Initializes a new square object with the given attribute.

        Args:
            size (int) : Private instance attribute.
                The size of a new square object.
        """
        self.__size = size
