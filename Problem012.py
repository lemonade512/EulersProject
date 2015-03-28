#!/usr/bin/env python

from Algorithms.NumericalAlgorithms.Python.divisors import divisors

def triangle_number(n):
    """ Returns the n'th triangle number. """
    return sum(range(n+1))

if __name__ == "__main__":
    i = 1
    t_num = 0
    while True:
        t_num = triangle_number(i)
        divs = divisors(t_num)
        if len(divs) >= 500:
            break
        i += 1
    print t_num
