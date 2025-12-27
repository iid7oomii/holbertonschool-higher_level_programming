#!/usr/bin/env python3
"""
A module that provides functionality to serialize a Python dictionary
to an XML file and deserialize an XML file to a Python dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: A dictionary with the deserialized data from the XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
            
        return result_dict
    except Exception:
        return None
