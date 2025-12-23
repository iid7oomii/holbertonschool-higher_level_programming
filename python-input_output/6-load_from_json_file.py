#!/usr/bin/python3
"""import json"""
import json


def load_from_json_file(filename):
    """create object from json"""
    with open(filename, "r") as f:
        return (json.load(f))
