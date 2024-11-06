#!/usr/bin/python3
"""This module contains one function"""

import sys


def makeChange(coins, total):
    """ Calculate the least bumber of coins needed to
    give change.
    """
    if total <= 0:  # return 0 if total is less than or equal to zero
        return 0
    max_coins = [0] + [sys.maxsize] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            max_coins[i] = min(max_coins[i], max_coins[i - coin] + 1)
    if max_coins[-1] != sys.maxsize:
        return max_coins[-1]
    else:
        return -1
