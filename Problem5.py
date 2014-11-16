#!/usr/bin/env python

from math import sqrt

def is_divisible(n):
    for i in xrange(1, 21):
        if float(n) % i != 0:
            return False

    return True

if __name__ == "__main__":
    print "Not yet implemented"
    #print divisors(20)
    #n = 20
    #while True:
    #    n += 20
    #    print n
    #    if is_divisible(n):
    #        print "n"
    #        break

    #print n
