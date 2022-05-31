#!/usr/bin/python3
"""
Define the to_json_string function
"""
import json


def to_json_string(my_obj):
    """ The function returns the JSON representation
    of an object (string) """
    return json.dumps(my_obj)
