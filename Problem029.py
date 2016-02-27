#!/usr/bin/env python

if __name__ == "__main__":
    A_MIN = 2
    A_MAX = 100
    B_MIN = 2
    B_MAX = 100

    terms = set()
    for i in xrange(A_MIN, A_MAX+1):
        for j in xrange(B_MIN, B_MAX+1):
            terms.add(i**j)

    print len(terms)
