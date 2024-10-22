#!/usr/bin/python3
"""This script that reads stdin line by line
and computes metrics
"""


from sys import stdin



stat_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

total_size = i = 0


def printr():
    """This function will print the stats"""
    print(f'File size: {total_size}')
    for key, value in sorted(stat_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))

try:
    for line in stdin:
        split_line = line.split()
        if len(split_line) >= 2:
            status = split_line[-2]
            total_size += int(split_line[-1])
            if status in stat_codes:
                stat_codes[status] += 1
        i += 1

        if i % 10 == 0:
            printr()
    printr()
except KeyboardInterrupt as e:
    printr()
