#!/usr/bin/python3
''' Minimum Operations '''
from typing import List


def minOperations(n: int) -> List[int]:
    """
    min Operations
    """
    if (n < 2 or not isinstance(n, int)):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
