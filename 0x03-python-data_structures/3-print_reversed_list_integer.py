#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list), 0, -1):
        if i >= 0:
            print("{:d}".format(i))
