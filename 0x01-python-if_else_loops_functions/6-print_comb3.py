#!/usr/bin/python3
for idx in range(10):
    for jdx in range(idx, 10):
        if idx < jdx:
            print("{:d}{:d}".format(idx, jdx),
                    end="\n" if idx == 8 and jdx == 9 else ", ")
