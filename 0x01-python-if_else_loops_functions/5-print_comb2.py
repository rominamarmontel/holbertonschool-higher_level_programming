#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print("{:2d}".format(number), end=", ")
    else:
        print("{:d}".format(number))
