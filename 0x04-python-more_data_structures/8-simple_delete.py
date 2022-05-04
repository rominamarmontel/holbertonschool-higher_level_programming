#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for element in a_dictionary:
        if element == key:
            del a_dictionary[element]
            return a_dictionary
    return a_dictionary
