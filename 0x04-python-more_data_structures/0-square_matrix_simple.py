#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda submatrixy: list(map(lambda px: px**2, submatrixy)), matrix))
