#!/usr/bin/python3
""" Module Base """
import os
import sys
import json

from traitlets import Instance


class Base:
    """ Define Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of class Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Definition of static method to_jason_string
            Returns: the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Definition of static method save_to_file
            writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        new_list_objs = []
        for i in list_objs:
            new_list_objs.append(i.to_dictionary())
        make_string = cls.to_json_string(new_list_objs)
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(make_string)

    @staticmethod
    def from_json_string(json_string):
        """ Definition of static method from_json_string
            Return: the list of the JSON string representation json_string """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Definition of class method create
            Return: an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Definition of class method load_from_file
            Return: returns a list of instances """
        filename = cls.__name__ + ".json"
        with open(filename, 'r', encoding='utf-8') as f:
            read_file = f.read()
            my_list = cls.from_json_string(read_file)
            new_list = []
            for instance in my_list:
                new_list.append(cls.create(**instance))
            return new_list
