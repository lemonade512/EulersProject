#!/usr/bin/env python

if __name__ == "__main__":
    nums = []
    for num in xrange(1001):
        if num % 3 == 0 or num % 5 == 0:
            nums.append(num)
    print sum(nums)
