#!/usr/bin/env python

from math import sqrt
from prime import is_prime

# TODO check problem forums to make sure all of this is implemented correctly

def prime_factors(num):
    factors = []
    for i in xrange(2, int(sqrt(num)) + 1):
        if is_prime(i) and num % i == 0:
            factors.append(i)
    return factors

if __name__ == "__main__":
    answer = prime_factors(600851475143)[-1]
    print answer
