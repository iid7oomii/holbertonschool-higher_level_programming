#!/usr/bin/python3
"""
Module 0-add_integer
Contains one function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
