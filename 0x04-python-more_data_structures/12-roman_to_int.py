#!/usr/bin/python3
def roman_to_int(roman_string):
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    pre = 0
    for i in range(len(roman_string) - 1, -1, -1):
        char = roman_string[i]
        if char not in dico or char is None:
            return 0
        num = dico[char]
        if num >= pre:
            sum += num
            pre = num
        else:
            sum -= num
    return sum
