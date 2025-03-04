#!/usr/bin/python3
# 101-nqueens.py task
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list representing the chessboard.
    solutions (list): A list of solutions.
Solutions are represented in the format [[k, l], [k, l], [k, l], [k, l]]
where `k` and `l` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `v`x`v` sized chessboard with 0's."""
    board = []
    [board.append([]) for p in range(v)]
    [row.append(' ') for p in range(v) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of the board."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of representation of a solved chessboard."""
    solution = []
    for k in range(len(board)):
        for l in range(len(board)):
            if board[k][l] == "Q":
                solution.append([k, l])
                break
    return (solution)


def xout(board, row, col):
    """Z out spots on a chessboard.
    All spots where queens can no
    longer be played are Z-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # Z out all forward spots
    for l in range(col + 1, len(board)):
        board[row][l] = "z"
    # Z out all backwards spots
    for l in range(col - 1, -1, -1):
        board[row][l] = "z"
    # Z out all spots below
    for k in range(row + 1, len(board)):
        board[k][col] = "z"
    # Z out all spots above
    for k in range(row - 1, -1, -1):
        board[k][col] = "z"
    # Z out all spots diagonally down to the right
    l = col + 1
    for k in range(row + 1, len(board)):
        if l >= len(board):
            break
        board[k][l] = "z"
        l += 1
    # Z out all spots diagonally up to the left
    l = col - 1
    for k in range(row - 1, -1, -1):
        if l < 0:
            break
        board[k][l]
        l -= 1
    # Z out all spots diagonally up to the right
    l = col + 1
    for k in range(row - 1, -1, -1):
        if l >= len(board):
            break
        board[k][l] = "z"
        k += 1
    # X out all spots diagonally down to the left
    l = col - 1
    for k in range(row + 1, len(board)):
        if l < 0:
            break
        board[k][l] = "z"
        l -= 1


def recursive_solve(board, row, queens, solutions):
    """Solve an N-queens recursive puzzle.
    Args:
        board (list): The current chessboard.
        row (int): The current row.
        queens (int): The current placed queens.
        solutions (list): A list of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for l in range(len(board)):
        if board[row][l] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, l)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
