#!/usr/bin/env python

def sum_of_squares(n):
    s = 0
    for i in range(n+1):
        s += i**2

    return s

def square_of_sum(n):
    s = 0
    for i in range(n+1):
        s += i
    s = s**2
    return s

if __name__ == "__main__":
    print square_of_sum(100) - sum_of_squares(100)
