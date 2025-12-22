#!/usr/bin/python3
"""Write text into file"""


def append_write(filename="", text=""):
    "Write text in the end of file"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
