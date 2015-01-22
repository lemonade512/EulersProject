#!/usr/bin/env python

# TODO look into how big integers are actually manipulated in languages
#      like Java and C++

total = 1
for i in range(1, 101):
    total *= i

sum_ = 0
while total > 0:
    num = total % 10
    sum_ += num
    total /= 10

print sum_
