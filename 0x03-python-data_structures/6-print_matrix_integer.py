#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submatrix in matrix:
        if len(submatrix) == 0:
            print()
        for px in range(len(submatrix)):
            print("{:d}".format(submatrix[px]), end="\n" if px is len(submatrix) - 1 else " ")
