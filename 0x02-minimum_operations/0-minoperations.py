#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed to result
"""


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    clipboard = 'H'
    current_text = 'H'
    operations = 0
    while len(current_text) < n:
        if n % len(current_text) == 0:
            operations += 2
            clipboard = current_text
            current_text += current_text
        else:
            operations += 1
            current_text += clipboard
    if len(current_text) != n:
        return 0
    return operations
