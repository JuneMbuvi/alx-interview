#!/usr/bin/python3
"""method that calculates the fewest number of operations needed
to result in exactly n H characters"""


def minOperations(n):
    """Returns an integer
    If n is impossible to achieve, return 0"""
    if n <= 2:
        return 0
    factors = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factors.append(i)
    return sum(factors)
