#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listdivi = []
    for px in my_list:
        if (px % 2) == 0:
            listdivi.append(True)
        else:
            listdivi.append(False)
        return listdivi
