#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = number % - 10
if last > 5:
    print("{0:d} is {1:d} and is greater than 5".format(number, last))
elif last == 0:
    print("{:d} is 0 and is 0".format(number))
else:
    print("{0:d} is {1:d} and is less than 6 and not 0".format(number, last))
