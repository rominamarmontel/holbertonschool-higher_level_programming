#!/usr/bin/python3
import json
"""
Define the save_to_json_file function
"""


def save_to_json_file(my_obj, filename):
    """ The function writes an Object to a text file,
    using a JSON representation """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
