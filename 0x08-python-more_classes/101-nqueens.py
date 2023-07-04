#!/usr/bin/env python3
"""
Solve the N queens problem.

Usage: nqueens N
where N must be an integer greater or equal to 4
"""

import sys


def print_board(board):
    """
    Print the given board in a human-readable way.
    """
    for row in board:
        print(' '.join(map(str, row)))


def is_valid(board, row, col):
    """
    Return True if the given row and column are valid for a queen.
    """
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if abs(row - i) == abs(col - board[i][col]):
            return False
    return True


def solve(board, row):
    """
    Solve the N queens problem recursively.
    """
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            solve(board, row + 1)
            board[row][col] = '.'


def main():
    """
    Parse the command-line arguments and solve the N queens problem.
    """
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solve(board, 0)


if __name__ == '__main__':
    main()