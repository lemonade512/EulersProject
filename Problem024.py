#!/usr/bin/env python

from itertools import permutations

#TODO implement an actual permutation algorithm and add it to Algorithms project
def lex_permutations(digits):
    """ Generates permutations of digits in lexicographic order.

    Args:
        digits: A list of digits (or characters)
    """
    sorted_digits = sorted(digits)
    for num in permutations(sorted_digits):
        yield num

if __name__ == "__main__":
    gen = lex_permutations([0,1,2,3,4,5,6,7,8,9])
    for i in range(999999):
        next(gen)

    print next(gen)

