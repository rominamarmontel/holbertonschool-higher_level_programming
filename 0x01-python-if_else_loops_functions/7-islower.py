#!/usr/bin/python3
def islower(c):
    c = ord(c)
    for min in range(97, 123):
        if c is min:
            return True
        else:
            return False
