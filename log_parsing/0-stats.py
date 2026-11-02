#!/usr/bin/python3
"""
Log parsing module: reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print the total file size and the number of lines
    by status code, in ascending order of status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))
    sys.stdout.flush()


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in status_codes:
                    status_codes[parts[-2]] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
