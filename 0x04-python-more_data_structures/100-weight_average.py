#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    i = 0
    j = 0
    for x, y in my_list:
        i += x * y
        j += y
    return i / j
