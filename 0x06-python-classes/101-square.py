#!/usr/bin/python3
"""
Module 101-square.py.

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

        position (tuple) : Private instance attribute.
            A tuple of 2 positive integers that defines the position of
            the square.

    Methods:
        __init__(self, size=0, position=(0, 0)) :
            Initializes a new square object with the given attributes.

        size(self) : @property
            Gets the property `size`.

        size(self, value) : @size.setter
            Sets the property `size`.

        position(self) : @property
            Gets the property `position`.

        position(self, value) : @position.setter
            Sets the property `position`.

        area(self) :
            Returns the current square area.

        my_print(self) :
            Prints in stdout the square with the character `#`.

        __str__(self) :
            Prints a string representation of the square object.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square object with the given attributes.

        Args:
            size (int) : Private instance attribute.
                The size of a new square object. The default value = 0.

            position (tuple) : Private instance attribute.
                A tuple of 2 positive integers that defines the position of
                the square. The default value = (0, 0).

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        This method gets the property `position`.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the property `position`.

        Args:
            value (tuple) : Private instance attribute.
                A tuple of 2 positive integers that defines the position of
                the square.

        Raises:
            TypError:
                If `value` is not a tuple.
                If len(value) != 2.
                If `value[0]` and `value[1]` are not integers.
                If `value[0]` and `value[1]` are less than zero.

        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or value[0] < 0
            or not isinstance(value[1], int)
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

        If the size = 0, an empty line is printed. The square is printed at
        the position specified by `position`.
        """
        if self.__size == 0:
            print("")
        else:
            height = self.__size + self.position[1]
            width = self.__size + self.__position[0]
            for y in range(height):
                if y < self.__position[1]:
                    print("")
                else:
                    for x in range(width):
                        if x < self.__position[0]:
                            print(" ", end="")
                        else:
                            print("#", end="")
                    print("")

    def __str__(self):
        """
        Prints a string representation of the square object.

        It has the same behavior as the method `my_print(self)`.
        """
        square_string = ""

        if self.__size == 0:
            return square_string
        else:
            height = self.__size + self.position[1]
            width = self.__size + self.__position[0]
            for y in range(height):
                if y < self.__position[1]:
                    square_string += "\n"
                else:
                    for x in range(width):
                        if x < self.__position[0]:
                            square_string += " "
                        else:
                            square_string += "#"
                    if y == (height - 1):
                        continue
                    else:
                        square_string += "\n"

        return square_string
