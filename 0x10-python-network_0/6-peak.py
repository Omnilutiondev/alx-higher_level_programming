#!/usr/bin/python3
""" This function finds a peak within a list of unsorted integers """


def find_peak(list_of_integers):
    """ find the number with the shortest algorithm"""
    if list_of_integers == []:
        return None

    idx = len(list_of_integers)
    if idx == 0:
        return (None)
    elif idx == 1:
        return (list_of_integers[0])
    elif idx == 2:
        return max(list_of_integers)

    med = int(idx/2)
    pk = list_of_integers[med]
    mylist = list_of_integers
    if pk > mylist[med - 1] and pk > mylist[med + 1]:
        return pk
    elif pk < mylist[med - 1]:
        return find_peak(mylist[:med])
    else:
        return find_peak(mylist[med + 1:])
