#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def generate_solutions(row, column):
    """
    Generates all possible solutions for placing row number of queens
    """
    # Initialize an empty solution each represented as a list of column
    # indices for each row
    solution = [[]]
    for queen in range(row):
        # for each function it calls place_queen which returns all possible
        # safe positions for the current queen.
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Used to find all the safe positions for a given queen on a chessboard
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if isSafe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def isSafe(q, x, array):
    """
    Used to check if it's safe to place a queen at a specific column in
    the current row
    Args:
        - q: current row
        - x: current column
        - array: current placement of queens in previous rows
    """
    if x in array:
        return False
    else:
        """
        for column in range(q) - Iterates over each column index up to the
        current row q.
        abs(array[column] - x) != q - column - checks if the absolute diff.
        btw. the current column and the column of any other queen array[column]
        is not equal to the diff. btw. their rows.This condition checks if the
        current position is on the same diagonal with any other queen.
        all() - this ensures that the condition inside is True  for all queens.
        """
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Initialize the program by checking the command line args and validating
    them.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    """
    Solves the N_Queens problem.
    """
    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == "__main__":
    n_queens()
