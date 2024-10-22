#!/usr/bin/python3
"""
Initialize variables to keep track of total file size and status code counts
"""

import sys


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_metrics():
    """Prints the total file size and counts of status codes in ascending order."""
    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
    raise
print_metrics()

