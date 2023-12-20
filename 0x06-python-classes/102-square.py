#!/usr/bin/python3
"""
Module 102-square.py.

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

        area(self) : The Area property.
            Returns the current square area.

        __eq__(self, other) : The "==" comparator.
            Checks if one square object is equal to another square object.

        __ne__(self, other) : The "!=" comparator.
            Checks if one square object is not equal to another square
            object.

        __gt__(self, other) : The ">" comparator.
            Checks if one square object is greater than another square object.

        __ge__(self, other) : The ">=" comparator.
            Checks if one square object is greater than or equal to another
            square object.

        __lt__(self, other) : The "<" comparator.
            Checks if one square object is less than another square object.

        __le__(self, other) : The "<=" comparator.
            Checks if one square object is less than or equal to another
            square object.
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
            size (int): Private instance attribute.
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

    def __eq__(self, other):
        """
        The "==" comparator.

        Checks if one square object is equal to another square object.

        Returns:
            result (bool) :
                True, if both square instances have equal areas.
                False, if otherwise.
        """
        if self.area() == other.area():
            result = True
        else:
            result = False

        return result

    def __ne__(self, other):
        """
        The "!=" comparator.

        Checks if one square object is not equal to another square
        object.

        Returns:
            result (bool) :
                True, if both square instances have unequal areas.
                False, if otherwise.
        """
        if self.area() != other.area():
            result = True
        else:
            result = False

        return result

    def __gt__(self, other):
        """
        The ">" comparator.

        Checks if one square object is greater than another square object.

        Returns:
            result (bool) :
                True, if the area of the first square instance is greater
                than the area of the second square instance.
                False, if otherwise.
        """
        if self.area() > other.area():
            result = True
        else:
            result = False

        return result

    def __ge__(self, other):
        """
        The ">=" comparator.

        Checks if one square object is greater than or equal to another
        square object.

        Returns:
            result (bool) :
                True, if the area of the first square instance is greater
                than or equal to the area of the second square instance.
                False, if otherwise.
        """
        if self.area() >= other.area():
            result = True
        else:
            result = False

        return result

    def __lt__(self, other):
        """
        The "<" comparator.

        Checks if one square object is less than another square object.

        Returns:
            result (bool) :
                True, if the area of the first square instance is less than
                the area of the second square instance.
                False, if otherwise.
        """
        if self.area() < other.area():
            result = True
        else:
            result = False

        return result

    def __le__(self, other):
        """
        The "<=" comparator.

        Checks if one square object is less than or equal to another square
        object.

        Returns:
            result (bool) :
                True, if the area of the first square instance is less than
                or equal to the area of the second square instance.
                False, if otherwise.
        """
        if self.area() <= other.area():
            result = True
        else:
            result = False

        return result
