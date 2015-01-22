#!/usr/bin/env python

if __name__ == "__main__":
    num_str = str(2**1000)
    s = 0
    for c in num_str:
        s += int(c)
    print s
