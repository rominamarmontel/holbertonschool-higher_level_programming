#!/usr/bin/python3
for number in range(0, 90):
    digit1 = number / 10
    digit2 = number % 10
    if number == 89:
        print(89)
    elif digit1 < digit2:
        print("{:02d}, ".format(number), end="")
