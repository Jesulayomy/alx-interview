#!/usr/bin/python3
""" N Queens Interview Question """

import sys


try:
    queens = int(sys.argv[1])
except IndexError:
    print("Usage: nqueens N")
    exit(1)
except ValueError:
    print("N must be a number")
    exit(1)
else:
    if queens and queens < 4:
        print("N must be at least 4")
        exit(1)

