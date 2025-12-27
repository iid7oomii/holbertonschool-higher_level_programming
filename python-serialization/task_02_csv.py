#!/usr/bin/env python3
"""
A module to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file
    named 'data.json'.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False if the
              file was not found or an error occurred.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True
    except FileNotFoundError:
        return False
