from prime import is_prime

def func(a, b, n):
    return (n ** 2) + (a * n) + b

def count_consecutive_primes(a, b):
    idx = 0
    while is_prime(abs(func(a, b, idx))):
        idx += 1

    return idx

max_count = 0
max_i = 0
max_j = 0
for i in xrange(-1000, 1000):
    for j in xrange(-1000, 1000):
        c = count_consecutive_primes(i, j)
        if c > max_count:
            max_count = c
            max_i = i
            max_j = j


print max_i * max_j

