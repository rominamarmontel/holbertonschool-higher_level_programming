#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    i = 1
    if __name__ == '__main__':
        argc = len(argv) - 1
        if argc == 0:
            print("0 argument.")
        elif argc == 1:
            print("1 argument:")
            print("{}: {}".format(i, argv[i]))
        else:
            print("{} arguments:".format(argc))
            for argument in range(1, len(argv)):
                print("{}: {}".format(i, argv[i]))
                i += 1
