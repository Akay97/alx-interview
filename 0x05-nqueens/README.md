# 0x05. N Queens

## Project Overview
The **N Queens** problem is a well-known algorithmic puzzle in computer science and mathematics. The goal is to place `N` queens on an `N×N` chessboard so that no two queens can attack each other. This project demonstrates the use of the **backtracking algorithm** to explore all potential solutions to this problem and is a classic example of recursion in action.

### Key Concepts
- **Backtracking**: The N Queens problem is solved using a backtracking algorithm, which explores each possible solution and backtracks when a solution path fails.
- **Recursion**: The solution utilizes recursive function calls to implement backtracking.
- **List Manipulation**: Lists are used to keep track of queens' positions on the chessboard.
- **Python Command Line Arguments**: Command-line arguments are used to input the value of `N`, and the `sys` module helps handle these arguments.

### Prerequisites
Make sure you have a basic understanding of the following concepts:
- Backtracking Algorithms
- Recursion in Python
- List Manipulations in Python
- Handling Command Line Arguments with `sys`

## Requirements
- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Execution Environment**: Ubuntu 20.04 LTS with Python 3 (version 3.4.3)
- **File Requirements**:
  - All files should end with a newline.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - Follow PEP 8 style guidelines (version 1.7.*).
  - All files must be executable.
- **README.md**: A README file at the root of the project folder is mandatory.

## Usage
To run the program, use the following syntax:
```bash
./nqueens N
