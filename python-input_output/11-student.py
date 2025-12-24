#!/usr/bin/python3
"""defines class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation with filter"""
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict[key]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
