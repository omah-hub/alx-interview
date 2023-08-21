#!/usr/bin/python3


""" A method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    The letter H is the only character in a text file.
"""


def minOperations(n):
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1
    return nOpei
