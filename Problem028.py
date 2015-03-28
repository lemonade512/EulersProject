#!/usr/bin/env python

if __name__ == "__main__":
    TARGET_NUM = 1001 * 1001
    #TARGET_NUM = 5 * 5
    sum_ = n = 1
    num_to_add = 2
    while n < TARGET_NUM:
        for i in xrange(4):
            n = n + num_to_add
            sum_ += n
        num_to_add += 2

    print sum_
