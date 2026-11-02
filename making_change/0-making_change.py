#!/usr/bin/python3
"""
Change comes from within module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet total.
    Return 0 if total is 0 or less, and -1 if total cannot be met
    by any number of the given coins.
    """
    if total <= 0:
        return 0

    coins = sorted(set(c for c in coins if 0 < c <= total))
    if not coins:
        return -1

    inf = total + 1
    dp = [0] + [inf] * total

    for coin in coins:
        for amount in range(coin, total + 1):
            prev = dp[amount - coin] + 1
            if prev < dp[amount]:
                dp[amount] = prev

    return dp[total] if dp[total] != inf else -1
