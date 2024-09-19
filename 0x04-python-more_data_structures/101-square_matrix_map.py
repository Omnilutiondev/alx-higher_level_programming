#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda px: list(map(lambda px: px**2, px)), matrix))
