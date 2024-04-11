#!/usr/bin/python3
"""program that solves the N queens problem"""
import sys


def is_safe(board, row, col):
    """Checks if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


def solve_n_queens(n):
    result = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            result.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return result


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
