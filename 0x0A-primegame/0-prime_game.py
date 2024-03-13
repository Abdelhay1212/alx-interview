#!/usr/bin/python3
''' Prime Game '''
from typing import Union, List


def isWinner(x: int, nums: List[int]) -> Union[str, None]:
    '''return the winner or None'''
    def countPrimes(n: int) -> bool:
        ''''''
        if n < 2:
            return False
        p = 2
        prime = [True] * (n+1)
        prime[0] = prime[1] = False
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        return prime.count(True)

    ben, maria = 0, 0
    for i in range(x):
        count = countPrimes(nums[i])
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None
