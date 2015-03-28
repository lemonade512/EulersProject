#!/usr/bin/env python

from Algorithms.NumericalAlgorithms.Python.division import long_division

if __name__ == "__main__":
    best_d = 0
    longest_repeat = 0
    for i in xrange(1, 1000):
        int_, dec, repeat = long_division(1, i)
        if len(str(repeat)) > longest_repeat:
            longest_repeat = len(str(repeat))
            best_d = i
    print best_d
