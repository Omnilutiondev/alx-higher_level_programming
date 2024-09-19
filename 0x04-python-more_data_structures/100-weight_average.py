#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(px * py for px, py in my_list) / sum(py for px, py in my_list))
