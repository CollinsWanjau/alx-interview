#!/usr/bin/env python3
import sys
# Initialization
def printSolution(board):
    result = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                result.append([i, j])
    # if all queens are placesd, print the placement of queens
    print(result)

def isSafe(board, row, col):
    """
    - Used to determine if a queen can be placed on a given position on the
    chessboard without being attacked by another queen
    Args:
        - board
        - row
        - col
    """
    # checks all cells to the left in the same row
    for i in range(col):
        # if there's a queen in any of these cells, it's not safe
        if board[row][i] == 1:
            return False
    
    # checks each cell in the upper left diagonal from current cell
    # specified by row and col.
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        # if any of these cells already has a queen, then it's not safe
        # to place a queen at the current cell bec two queens cannot be in
        # the same diagonal.
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solveNQUtil(board, col):
    """
    BackTracking, placement and recursion
    This function solves the NQueens problem. It tries to place a queen each
    row of the current column and then recursively call itself for the next
    column.
    If it can't find a safe spot in the current column or if placing a queen
    in the current spot leads to no solution, it backtracks by removing the
    queen from the current spot and coninues to the next row
    """
    # Base Case: If all queens are placed then return true
    if col >= N:
        printSolution(board)
        return True
    res = False
    # try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            # Recursion
            res = solveNQUtil(board, col + 1) or res
            # Backtracking
            board[i][col] = 0
    return res

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solveNQUtil(board, 0):
        return False
    return True

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

if __name__ == '__main__':
    solveNQ()