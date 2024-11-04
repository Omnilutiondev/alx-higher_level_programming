#!/usr/bin/python3
for idx in range(25, -1, -1):
    cdx = idx + ord('A')
    if idx % 2 == 1:
        cdx += 32
    print("{:c}".format(cdx), end="")
