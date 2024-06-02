#!/usr/bin/python3
'''
Pascal triangle function
'''


def pascal_triangle(n):
    '''
    Returns a list of lists representing the pascal triangle of n
    '''
    # If n is less than 0 return an empty list
    if n <= 0:
        return []

    # The first list will always be 1
    res = [[1]]


    for i in range(n - 1):
        # Add 0 at the start and the end of a temp list
        temp = [0] + res[-1] + [0]

        # Create list for storing the new values
        row = []

        # Loop through the new number of elements adding the two top
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])

        # Append the list to the results list
        res.append(row)

    return res
