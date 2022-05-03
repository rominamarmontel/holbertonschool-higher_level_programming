#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if 0 <= idx < len(my_list):
            return my_list[idx]
    return None
