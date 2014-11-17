#!/usr/bin/env python

def get_nums(filename):
    nums = []
    f = open(filename)
    for line in f:
        nums.append(int(line))

    return nums

if __name__ == "__main__":
    num = sum(get_nums("Problem13_input.txt"))
    print str(num)[:10]
