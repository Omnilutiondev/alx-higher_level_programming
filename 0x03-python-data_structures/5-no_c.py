#!/usr/bin/python3
def no_c(my_string):
    rem = ""
    for px in range(len(my_string)):
        if (my_string[px] != 'c' and my_string[px] != 'C'):
            rem += my_string[px]
        return rem
