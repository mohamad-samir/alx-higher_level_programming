#!/usr/bin/python3

"""
module for calculation of n-queens problem
"""
import sys


class Solution_Board:
    """
    class for use with n queens problem
    """
    solutions = []

    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise TypeError("num should be an int")
        self.__num = value


args = sys.argv


if len(args) != 2:
    exit(1)
if not args[1].isdigit():
    print("N must be a number")
    exit(1)

num = int(args[1])
if num < 4:
    print("N must be at least 4")
    exit(1)

solutions = []
board = [[0 for _ in range(0, num)] for _ in range(0, num)]


def get_n_queens(chess_board, column=0, num=0):
    if column >= num:
        return True
    for i in range(0, num):
        if board_safe(chess_board, i, column):
            chess_board[i][column] = 1
            if get_n_queens(chess_board, column + 1, num):
                return True
            chess_board[i][column] = 0
    return False


def board_safe(chess_board, row, column):
    # Check if there is a queen in the same column
    for i in range(row):
        if chess_board[i][column] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row
    j = column
    while i >= 0 and j >= 0:
        if chess_board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row
    j = column
    while i >= 0 and j < num:
        if chess_board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


running = True
while running:
    sol = get_n_queens(board, column=0, num=num)
    if sol:
        solutions.append([list(row) for row in board])
    else:
        running = False

# Print the solutions
for solution in solutions:
    print(solution)
