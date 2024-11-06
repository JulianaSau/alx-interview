#!/usr/bin/python3

"""
 this module contains one function validate if
 a string is a valid utf8 string
"""
NUMBER_OF_BITS_PER_BLOCK = 8
MAX_NUMBER_OF_ONES = 4


def validUTF8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= NUMBER_OF_BITS_PER_BLOCK - 1
        if number == 0:  # single byte char
            index += 1
            continue

        # validate multi-byte char
        number_of_ones = 0
        while True:  # get the number of significant ones
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= NUMBER_OF_BITS_PER_BLOCK - number_of_ones - 1
            if number == 1:
                number_of_ones += 1
            else:
                break

            if number_of_ones > MAX_NUMBER_OF_ONES:
                return False  # too much ones per char sequence

        if number_of_ones == 1:
            return False  # there has to be at least 2 ones

        index += 1

        # check for out of bounds and exit early
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False

        # every next byte has to start with "10"
        for i in range(index, index + number_of_ones - 1):
            number = data[i]

            number >>= NUMBER_OF_BITS_PER_BLOCK - 1
            if number != 1:
                return False
            number >>= NUMBER_OF_BITS_PER_BLOCK - 1
            if number != 0:
                return False

            index += 1

    return True
