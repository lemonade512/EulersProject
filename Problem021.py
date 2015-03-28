#!/usr/bin/env python

import cProfile
from math import sqrt

from Algorithms.NumericalAlgorithms.Python.divisors import divisors

# d(n) is the sum of proper divisors of n
def d(n):
    return sum(divisors(n)[:-1])

def is_amicable(n):
    d_n = d(n)
    d_d_n = d(d_n)
    if n == d_d_n and n != d_n:
        return True

    return False

def run():
    total = 0
    for num in xrange(10000):
        if is_amicable(num):
            total += num

    print total

if __name__ == "__main__":
    run()
    #cProfile.run("run()")
