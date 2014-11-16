#!/usr/bin/env python

from math import sqrt

def triangle_number(n):
    """ Returns the n'th triangle number. """
    return sum(range(n+1))

def divisors(n):
    output = list()
    for i in range(1, int(sqrt(n))):
        if n == (n / i) * i:
            if i * i == n or i == 1:
                output.append(i)
            else:
                output.append(i)
                output.append(n/i)
    output.append(n)

    return sorted(output)

if __name__ == "__main__":
    i = 1
    t_num = 0
    while True:
        t_num = triangle_number(i)
        divs = divisors(t_num)
        if len(divs) >= 500:
            break
        i += 1
    print t_num
