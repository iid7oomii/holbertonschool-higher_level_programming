#!/usr/bin/python3
"""
Module that defines a Square class using properties (Getter and Setter).

This module centralizes size validation within the setter method.
"""


class Square:
    """
    The Square class represents a geometric square figure, utilizing
    properties to control access and modification
    of the private size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Calls the setter method to handle initial validation.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
        """
        # We use the setter to assign the initial value, ensuring validation
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The value of the private attribute __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square with validation.

        Args:
            value (int): The new side length of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        # Store the validated value in the private attribute
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The current area of the square (size * size).
        """
        return self.__size ** 2
