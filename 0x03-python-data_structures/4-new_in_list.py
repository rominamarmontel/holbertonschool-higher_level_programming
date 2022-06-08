#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if 0 > idx or idx > len(my_list):
        return my_list
    for i in new_list:
        new_list[idx] = element
        return new_list
