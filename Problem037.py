#!/usr/bin/env python

from Algorithms.Algorithms.NumericalAlgorithms.Python import primes
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

g_primes = [i for i in primes.prime_sieve(10000000)]
def is_truncatable(p):
    s = str(p)
    output = True
    for i, _ in enumerate(s):
        if binary_search(g_primes, int(s[i:])) == -1:
        #if not primes.is_prime(int(s[i:]), 10):
            output = False
            break
        if binary_search(g_primes, int(s[:i+1])) == -1:
        #elif not primes.is_prime(int(s[:i+1]), 10):
            output = False
            break

    return output

a = []
for n in xrange(10, 1000000):
    if is_truncatable(n):
        a.append(n)

print sum(a)

