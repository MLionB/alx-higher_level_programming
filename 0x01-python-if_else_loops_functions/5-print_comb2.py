#!/usr/bin/python3
for x in range(100):
    if x == 99:
        print("{0:0=2d}".format(x))
    else:
        print("{0:0=2d}".format(x), end=", ")
