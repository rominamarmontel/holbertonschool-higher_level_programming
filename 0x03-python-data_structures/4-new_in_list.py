#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx not in my_list or element >= 0:
        new_list = my_list.copy()
        my_list[idx] = element
        return new_list
    else:
        return my_list