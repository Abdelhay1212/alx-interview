#!/usr/bin/python3
''' Minimum Operations '''
from typing import List


def prime_factors(n: int) -> List[int]:
    '''returns prime factors of n'''
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


def minOperations(n: int) -> int:
    '''Calculates the fewest number of operations needed
    to result in exactly n H characters'''
    if n <= 1 or not isinstance(n, int):
        return 0

    factors = set(prime_factors(n))
    min_operations = float('inf')

    for factor in factors:
        text = 'H'
        num_of_operations = 1

        while n != len(text):
            if factor == len(text):
                text += 'H' * factor
                num_of_operations += 2
            elif factor > len(text):
                text += 'H'
                num_of_operations += 1
            else:
                text += 'H' * factor
                num_of_operations += 1

        min_operations = min(min_operations, num_of_operations)

    return int(min_operations)
