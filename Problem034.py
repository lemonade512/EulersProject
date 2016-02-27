#!/usr/bin/env python

from Problem030 import digits

def factorial(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod


if __name__ == "__main__":
    # TODO needs some optimization
    i = 10
    nums_equal_factorial = []

    while True:
        factorial_digits = [factorial(d) for d in digits(i)]
        if len(factorial_digits) * factorial(9) < i:
            break

        if sum(factorial_digits) == i:
            nums_equal_factorial.append(i)

        i += 1

    print sum(nums_equal_factorial)
