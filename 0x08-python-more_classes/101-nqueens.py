#!/usr/bin/python3
"""A program that solves the N queens problem."""
import sys

def solve_nqueens(N):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check if there is a queen in the upper left diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check if there is a queen in the upper right diagonal
        i = row
        j = col
        while i >= 0 and j < N:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def backtrack(board, row):
        if row == N:
            # Found a solution, add it to the list of solutions
            solutions.append([list(row) for row in board])
            return True

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(board, row + 1)
                board[row][col] = 0

    # Initialize the board
    board = [[0] * N for _ in range(N)]
    solutions = []

    # Start the backtracking algorithm
    backtrack(board, 0)

    return solutions

if __name__ == "__main__":
    # Validate the input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print(solution)
