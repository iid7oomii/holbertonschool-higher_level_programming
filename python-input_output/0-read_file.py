#!/usr/bin/python3

"""Module that read a file"""

def read_file(filename=""):
    """Read the file from filename"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
