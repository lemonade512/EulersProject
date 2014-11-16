#!/usr/bin/env python

#TODO implement fibonacci number finder with cacheing or dynamic programming?

if __name__ == "__main__":
    nums = []

    n0 = 1
    n1 = 1
    while n0 < 4000000:
        new_n = n0 + n1
        if new_n < 4000000 and new_n % 2 == 0:
            nums.append(new_n)

        n0 = n1
        n1 = new_n

    print sum(nums)
