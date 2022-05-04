#!/usr/bin/python3
def roman_to_int(roman_string):
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for char in roman_string:
        if char not in dico or char is None:
            return 0
        num += dico[char]     
    return num
