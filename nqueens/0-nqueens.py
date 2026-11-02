#!/usr/bin/python3
"""
N queens module: prints every way to place N non-attacking
queens on an N x N chessboard
"""
import sys


def solve(n, row, cols, diag1, diag2, board, solutions):
    """
    Place a queen on each row using backtracking.
    cols, diag1 and diag2 hold the columns and diagonals
    already attacked; board holds the current placement.
    """
    if row == n:
        solutions.append([pos[:] for pos in board])
        return
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        board.append([row, col])
        solve(n, row + 1, cols, diag1, diag2, board, solutions)
        board.pop()
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, set(), set(), set(), [], solutions)
    for solution in solutions:
        print(solution)
