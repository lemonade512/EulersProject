#!/usr/bin/env python

from math import sqrt

def is_prime(num):
    if num == 1:
        return False

    for i in xrange(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

primes = []
def prime(num):
    """ Returns the num'th prime. """
    # TODO raise error if num is 0
    global primes
    if len(primes) >= num:
        return primes[num-1]

    last_prime = len(primes)
    if len(primes) == 0:
        i = 0
    else:
        i = primes[last_prime-1]
    while last_prime < num:
        i += 1
        if is_prime(i):
            last_prime += 1
            primes.append(i)

    return primes[-1]

if __name__ == "__main__":
    i = 1
    p_num = prime(i)
    s = 0
    while p_num < 2000000:
        s += p_num
        i += 1
        p_num = prime(i)
    print s
