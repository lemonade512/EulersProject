#!/usr/bin/env python

def is_palindrome(num):
    s = str(num)
    # reverse the string
    r_s = s[::-1]
    if s == r_s:
        return True

    return False

if __name__ == "__main__":
    largest_palindrome = 0
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    print largest_palindrome
