#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number) % 10
    if last < 0:
        print("{}".format(-last), end="")
        return -last
    else:
        print("{}".format(last), end="")
        return last
