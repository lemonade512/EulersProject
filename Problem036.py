#!/usr/bin/env python

def is_palindrome(p):
    s = str(p)
    rs = str(p)[::-1]
    return s == rs


if __name__ == "__main__":
    MAX = 1000000
    nums = []
    for i in range(1, MAX):
        b10 = is_palindrome(i)
        b2 = is_palindrome(bin(i)[2:])
        if b10 and b2:
            nums.append(i)

    print sum(nums)
