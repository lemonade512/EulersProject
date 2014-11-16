#!/usr/bin/env python

import datetime

# TODO make sure to actually do this problem in a non-cheap way :)
def find_sundays():
    count = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            d = datetime.datetime(i, j, 1, 0, 0, 0, 0)
            if d.weekday() == 6:
                count += 1

    return count

if __name__ == "__main__":
    print find_sundays()
