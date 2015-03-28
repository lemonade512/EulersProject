#!/usr/bin/env python

from Algorithms.NumericalAlgorithms.Python.divisors import divisors

def is_abundant(n):
    """ Returns whether or not `n` is an abundant number.

    An abundant number is a number whose proper divisors sum to
    be greater than the number itself.

    Examples:
        >>> is_abundant(12)
        True

    """
    return n < sum(divisors(n)[:-1])

if __name__ == "__main__":
    LIMIT = 28123
    abundant_nums = []
    for i in xrange(LIMIT + 1):
        if is_abundant(i):
            abundant_nums.append(i)

    abundant_sums = []
    for i, a_num in enumerate(abundant_nums):
        for num2 in abundant_nums[i:]:
            abundant_sums.append(a_num + num2)
    abundant_sums = list(set(abundant_sums))

    no_sum_nums = []
    for i in xrange(LIMIT):
        if i not in abundant_sums:
            no_sum_nums.append(i)

    print sum(no_sum_nums)
