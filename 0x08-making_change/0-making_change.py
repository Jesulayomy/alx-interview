#!/usr/bin/python3
""" Making Change interview task """


def makeChange(coins, total):
    """
        determine the fewest number of
        coins needed to meet a given amount total
    """

    if total <= 0:
        return 0

    for i in range(len(coins)):
        coin = 0
        amount = 0
        for coin in reversed(sorted(coins[i:])):
            while amount + coin <= total:
                amount += coin
                coin += 1
            if amount == total:
                return coin

    return -1
