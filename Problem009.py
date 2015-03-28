#!/usr/bin/env python

def is_pythagorean_triplet(a, b, c):
    if (a**2 + b**2) == c**2:
        return True
    return False

if __name__ == "__main__":
    triple = (0, 0, 0)
    for c in range(1000):
        # Can go up to c-1. If b = c then a = 0. Thus b != c.
        for b in range(c):
            # a be 0 to b
            for a in range(b+1):
                if (a+b+c) == 1000 and is_pythagorean_triplet(a, b, c):
                    triple = (a, b, c)

            if triple != (0, 0, 0):
                break
        if triple != (0, 0, 0):
            break

    print triple[0] * triple[1] * triple[2]
