#!/usr/bin/python3
"""
Defines a Square class based on the given requirements.
This module strictly enforces type and value checks on the size attribute.
"""


class Square:
    """
    The Square class represents a geometrical square figure.
    It is initialized with an optional size parameter, which must be a
    non-negative integer, and stores it as a private instance attribute.
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
