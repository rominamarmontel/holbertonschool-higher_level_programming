#!/usr/bin/python3
import json
"""
Define the from_json_string function
"""


def from_json_string(my_str):
    """ The function returns an object
    (Python data structure) represented by a JSON string """
    return json.loads(my_str)
