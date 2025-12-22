#!/usr/bin/python3
"""import json"""
import json


def save_to_json_file(my_obj, filename):
    """writes object into text file using json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
