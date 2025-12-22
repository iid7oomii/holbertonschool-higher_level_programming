#!/usr/bin/python3
"""write into file"""


def write_file(filename="", text=""):
    """open filename and write into text"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
