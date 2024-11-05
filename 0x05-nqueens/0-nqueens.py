#!/usr/bin/python3
"""
N queens puzzle
"""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row=0, board=[]):
    """Use backtracking to find all solutions for the N Queens problem."""
    if row == n:
        """Solution found, print it in the required format"""
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()

def main():
    """Check command-line arguments"""
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
    
    solve_nqueens(n)

if __name__ == "__main__":
    main()
