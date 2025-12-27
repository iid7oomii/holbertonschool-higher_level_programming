#!/usr/bin/env python3
"""
A module that defines a custom class CustomObject and demonstrates
how to serialize and deserialize instances of this class using the
pickle module.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and is_student.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): True if the person is a student, False otherwise.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in the following format:
        Name: <name>
        Age: <age>
        Is Student: <is_student>
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to the
        provided filename using the pickle module.

        Args:
            filename (str): The name of the file to save the serialized object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return an instance of CustomObject from the
        provided filename using the pickle module.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized instance of CustomObject, or
                          None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
