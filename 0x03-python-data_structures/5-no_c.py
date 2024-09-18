#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for px in range(len(my_string)):
        if (my_string[px] != 'c' and my_string[px] != 'C'):
            ret += my_string[px]

        return ret
