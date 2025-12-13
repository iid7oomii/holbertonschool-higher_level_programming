#!/usr/bin/python3
"""
Module that defines a Square class.

This module introduces validation for the size attribute and a public
method to calculate the square's area.
"""


class Square:
    """
    The Square class represents a geometric square figure.

    It is initialized with an optional size parameter, which must be a
    non-negative integer, and provides a method to calculate its area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        The size attribute is validated to ensure it is an integer >= 0.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        # Private instance attribute storage
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        The area is calculated using the formula: size * size.

        Returns:
            int: The current area of the square.
        """
        # The area of a square is side length squared.
        return self.__size ** 2
