#!/usr/bin/python3
"""
Minimum Operations module
"""


def minOperations(n):
    """
    Calculate the fewest number of Copy All / Paste operations
    needed to obtain exactly n 'H' characters, starting from one.
    Return 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    if n > 1:
        operations += n

    return operations
