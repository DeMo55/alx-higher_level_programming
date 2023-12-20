#!/usr/bin/python3
"""
Module 103-magic_class.py

This module has only one class.

Classes:
    MagicClass :
        A class representing a circle.

Functions:
    This module has no functions.
"""

import math


class MagicClass:
    """
    A class representing a circle.

    The class does exactly the same as a given Python bytecode.

    Attributes:
        radius (int, float) : Private instance attribute.
            The radius of the new circle instance.

    Methods:
        __init__(self, radius) :
            Initializes a new circle object with the given attribute.

        area(self) :
            Computes the area of the circle object.

        circumference(self) :
            Computes the circumference of the circle object.
    """

    def __init__(self, radius=0):
        """
        Initializes a new circle object with the given attribute.

        Arg:
            radius (int, float) : Private instance attribute.
                The radius of the new circle instance. The default value = 0
        """
        if (
            type(radius) is not int
            and type(radius) is not float
        ):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

        return None

    def area(self):
        """
        Computes the area of the circle object.

        Returns:
            circle_area (float) :
                The area of the circle based on its radius.
        """
        circle_area = (self.__radius ** 2) * math.pi

        return circle_area

    def circumference(self):
        """
        Computes the circumference of the circle object.

        Returns:
            circle_circumference (float) :
                The circumference of the circle based on its radius.
        """
        circle_circumference = 2 * math.pi * self.__radius

        return circle_circumference
