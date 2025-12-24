#!/usr/bin/python3
"""defines class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):

            new_dict = {}
            for key in attrs:
                if key in attrs:
                    if key in self.__dict__:
                        new_dict[key] = self.__dict__[key]

            return new_dict

        else:
            return self.__dict__
