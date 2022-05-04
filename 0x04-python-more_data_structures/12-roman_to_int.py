#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    pre = 0
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string) - 1, -1, -1):
        c = roman_string[i]
        if c not in dico or c is None:
            return 0
        n = dico[c]
        if n >= pre:
            num += n
            pre = n
        else:
            num -= n
    return num
