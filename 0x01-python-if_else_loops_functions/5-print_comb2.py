#!/usr/bin/python3
for idx in range(100):
    print("{:02d}".format(idx), end="\n" if idx == 99 else ", ")
