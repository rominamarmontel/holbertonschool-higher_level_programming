#!/usr/bin/python3
""" Module Node """


class Node:
    """ Definition of a Class Node
        Attributes :
                  data (int): data
    """
    def __init__(self, data, next_node=None):
        """initializes the Node
        Args:
            size (int): size of a side of the square
        """
        self.__data = data
        self.__next_mode = next_mode

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value == None or type(value) != Node:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """ Definition of a Class SinglyLinkedList
        Attributes :
                  data (int): data
    """
    def __init__(self):
        """initializes the SinglyLinkedList
        Args:
            head (): the head of a node
        """

    def sorted_insert(self, value):
        new = Node(value)
