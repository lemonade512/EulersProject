#!/usr/bin/env python

from math import sqrt

def is_prime(num):
    if num == 1:
        return False

    for i in xrange(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

