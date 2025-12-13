#!/usr/bin/python3
"""
Defines a Square class with properties for size and position,
and methods for area calculation and offset printing.
"""


class Square:
    """
    The Square class represents a geometrical square figure,
    managing its size and position via validated properties.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Sets the size and position attributes using the property setters
        to ensure validation is performed upon instantiation.

        Args:
            size (int, optional): The side length of the square. Defaults to 0.
            position (tuple, optional): The offset position (x, y).
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
            tuple: The current position (x, y) offset.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The new position (x, y) offset.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        is_valid_tuple = (
            isinstance(value, tuple) and
            len(value) == 2 and
            all(isinstance(i, int) and i >= 0 for i in value)
        )

        if not is_valid_tuple:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square figure to stdout using the '#' character,
        respecting the vertical (position[1]) and horizontal (position[0])
        offsets.

        Prints an empty line if the size is 0.
        """
        if self.__size == 0:
            print()
            return

        # تطبيق الإزاحة العمودية (Vertical Offset)
        for _ in range(self.__position[1]):
            print()

        # طباعة المربع مع الإزاحة الأفقية
        horizontal_offset = " " * self.__position[0]
        square_row = "#" * self.__size

        for _ in range(self.__size):
            print(horizontal_offset + square_row)
