#!/usr/bin/python3
"""Module that defines function minOperations
"""


def minOperations(n):
    """Calculates the minimum number of using the copy all and paste
    operations so a file can have n number of H character in the file

    Returns:
        number of operations
        or 0 if n < 2
    """
    min_ops = 2
    chars_num = 2
    copied = 1

    if n < 2:
        return 0

    while chars_num < n:
        rest = n % chars_num
        if rest % chars_num == 0:
            copied = chars_num
            min_ops += 2
            chars_num += copied
        else:
            chars_num += copied
            min_ops += 1

    return min_ops
