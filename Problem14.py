#!/usr/bin/env python

#TODO try to make this faster

def collatz_sequence(start):
    n = start
    output = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        output.append(n)
    return output

if __name__ == "__main__":
    max_len = 0
    max_start = 0
    for i in range(1000000):
        c_seq = collatz_sequence(i)
        if len(c_seq) > max_len:
            max_len = len(c_seq)
            max_start = i
    print max_start
