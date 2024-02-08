#!/usr/bin/python3
''' N queens '''

import sys


def Nqueens(n: int):
    ''' placing N non-attacking queens on an N*N chessboard '''
    res = []

    cols = set()
    posiDiag = set()
    negaDiag = set()

    q = []

    def backtrack(r):
        if r == n:
            copy = q.copy()
            res.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in posiDiag or (r - c) in negaDiag:
                continue

            cols.add(c)
            posiDiag.add(r + c)
            negaDiag.add(r - c)
            q.append([r, c])

            backtrack(r + 1)

            cols.remove(c)
            posiDiag.remove(r + c)
            negaDiag.remove(r - c)
            q.pop()

    backtrack(0)
    return res


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        num = int(args[1])
    except:
        print('N must be a number')
        exit(1)

    if num < 4:
        print('N must be at least 4')
        exit(1)

    res = Nqueens(num)
    for l in res:
        print(l)
