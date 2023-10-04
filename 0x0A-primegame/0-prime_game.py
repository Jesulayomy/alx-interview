#!/usr/bin/python3
""" Prime game  module between two users """


def isWinner(x, nums):
    """ Determines the winner in a game between two players """

    if not nums or x < 1:
        return None
    n = max(nums)
    nums.sort()
    primes = [True for i in range(n + 1)]
    c = 0
    for i in range(2, n + 1):
        if primes[i] is True:
            c += 1
            for j in range(i, n + 1, i):
                primes[j] = False
    wins = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        wins[i] = wins[i - 1]
        while c and nums[c - 1] >= i:
            wins[i] += 1
            c -= 1
    player1 = 0
    for n in nums:
        player1 += wins[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
