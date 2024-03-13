#!/usr/bin/python3
''' Prime Game '''


def isWinner(x, nums):
    '''return the winner or None'''
    def SieveOfEratosthenes(n):
        if n < 2:
            return False
        p = 2
        prime = [True] * (n+1)
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        return sum(prime[2:]) % 2 == 1

    ben, maria = 0, 0
    for num in nums:
        if SieveOfEratosthenes(num):
            maria += 1
        else:
            ben += 1

    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None


print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
