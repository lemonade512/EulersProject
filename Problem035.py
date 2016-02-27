#!/usr/bin/env python

from Algorithms.Algorithms.NumericalAlgorithms.Python.primes import is_prime, find_primes

from Problem030 import digits
from collections import deque

from bisect import bisect_left

#TODO shouldn't use global variable
#MAX = 100
MAX = 1000000
primes = find_primes(MAX)

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return pos if pos != hi and a[pos] == x else -1

def to_num(d):
    """ Converts a deque of digits to an integer. """
    num = 0
    d_copy = list(d)
    for i in range(0, len(d_copy)):
        num += (10**i) * d_copy.pop()
    return num

def all_rotations_prime(n):
    d = deque(digits(n))
    for _ in range(len(d)):
        if binary_search(primes, to_num(d)) < 0:
            return False
        d.rotate(1)

    return True

if __name__ == "__main__":
    count = 0
    for p in primes:
        if all_rotations_prime(p):
            count += 1

    print count
