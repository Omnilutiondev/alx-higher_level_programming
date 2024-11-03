#!/usr/bin/python3
for idx in range(ord('a'), ord('z') + 1):
    if idx != ord('q') and idx != ord('e'):
        print("{:c}".format(idx), end="")
