#!/usr/bin/env python

def read_num_from_file(filename):
    f = open(filename)
    num = f.readline()
    f.close()
    return num

def product_of_digits(string):
    s = 1
    for c in string:
        num = int(c)
        s *= num
    return s

if __name__ == "__main__":
    max_13_digits = "0"*13
    max_product = 0
    num_str = read_num_from_file("Problem008_input.txt")
    for i in range(len(num_str)-13):
        digits = num_str[i:i+13]
        product = product_of_digits(digits)
        if max_product < product:
            max_13_digits = digits
            max_product = product

    print max_product
