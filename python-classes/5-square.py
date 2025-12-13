#!/usr/bin/python3
"""
Defines a Square class with properties (getter/setter) for size,
and methods to calculate the area and print the square figure.
"""


class Square:
    """
    The Square class represents a geometrical square figure.

    It manages its size via properties to enforce validation rules.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Sets the size attribute using the property setter to ensure validation.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
            int: The current size (side length) of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Performs strict type and value validation.

        Args:
            value (int): The new side length for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square figure to stdout using the '#' character.

        Prints an empty line if the size is 0.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
