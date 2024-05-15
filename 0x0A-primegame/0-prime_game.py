#!/usr/bin/python3
"""determine who the winner of each prime game"""


def isWinner(x, nums):
    """name of the player that won the most rounds"""
    def isPrime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def gameWinner(primes, num):
        if num == 1 or not primes:
            return "Ben"
        elif num in primes:
            return "Maria"
        else:
            return "Maria" if num % 2 == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [num for num in range(2, n + 1) if isPrime(num)]
        winner = gameWinner(primes, n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
