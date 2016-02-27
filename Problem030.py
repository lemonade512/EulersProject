#!/usr/bin/env python

def digits(n):
    """ Calculates and returns a list of the digits of n.

    Args:
        n (int): The number to find the digits of.

    Returns:
        A list of integers between 0 and 9 inclusive.
    """
    n = str(n)
    digit_list = []
    for c in n:
        digit_list.append(int(c))

    return digit_list


if __name__ == "__main__":
    POWER = 5
    sum_ = 0
    i = 2
    while True:
        digits_to_pow = [d**POWER for d in digits(i)]

        if len(digits_to_pow) * (9**POWER) < i:
            # IF we reach here we can be sure that no more numbers need to
            # be checked because even with all 9's the digits could not
            # possibly add to the number
            break

        if sum(digits_to_pow) == i:
            sum_ += i
        i += 1

    print sum_
