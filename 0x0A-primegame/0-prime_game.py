#!/usr/bin/python3
"""defining a prime numbers game"""


def isWinner(x, nums):
    """determines the winner of the prime numbers game"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Initialize scores and arrays of possible prime numbers
    ben = 0
    maria = 0
    m = [1 for x in range(sorted(nums)[-1] + 1)]
    m[0], m[1] = 0, 0
    for i in range(2, len(m)):
        rm_multiples(m, i)

    for i in nums:
        if sum(m[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

        if ben > maria:
            return "Ben"
        if maria > ben:
            return "Maria"
        return None


def rm_multiples(ls, x):
    """removes multiples of a prime number from an
    array of possible solutions"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
