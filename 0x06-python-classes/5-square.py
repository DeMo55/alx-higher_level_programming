#!/usr/bin/python3
"""
Module 5-square.py.

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

        my_print(self) :
            Prints in stdout the square with the character `#`.
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
                If `size` is not an integer.
            ValueError:
                If `size` is less than zero.
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

    def my_print(self):
        """
        Prints in stdout the square with the character `#`.

        If the size = 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                square_line = ""
                for j in range(self.__size):
                    square_line += "#"
                print(square_line)
