#!/usr/bin/env python

from Problem030 import digits


def digits_pandigital_1to9(d_list):
    return sorted(d_list) == [1,2,3,4,5,6,7,8,9]


if __name__ == "__main__":
    # TODO find more mathematical way to figure out where to stop
    # TODO needs lots of optimizing :)
    pandigital_products = set()
    for i in xrange(1, 2000):
        for j in xrange(i, 2000):
            d_list = digits(i) + digits(j) + digits(i*j)
            if digits_pandigital_1to9(d_list):
                pandigital_products.add(i*j)

    print 7254 in pandigital_products
    print sum(pandigital_products)
