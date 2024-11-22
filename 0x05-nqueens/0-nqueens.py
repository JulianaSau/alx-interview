#!/usr/bin/python3
""" A function that positions N Queens on NxN chessboard"""


import sys


def build_solutions(row, col):
    soln = [[]]
    for qn in range(row):
        soln = position_queen(qn, col, soln)
    return soln


def position_queen(qn, col, prev_soln):
    safe_pos = []
    for arr in prev_soln:
        for n in range(col):
            if is_safe(qn, n, arr):
                safe_pos.append(arr + [n])
    return safe_pos


def is_safe(c, ar, arr):
    if ar in arr:
        return (False)
    else:
        return all(abs(arr[col] - ar) != c - col
                   for col in range(c))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    # generate all solutions
    solns = build_solutions(n, n)
    # print solutions
    for arr in solns:
        free = []
        for x, y in enumerate(arr):
            free.append([x, y])
        print(free)


if __name__ == '__main__':
    n_queens()
