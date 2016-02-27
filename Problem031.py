coins = [1, 2, 5, 10, 20, 50, 100, 200]

# ans(target) = sum(ans(target-coin) for coin in coins)
def answer(target):
    M = [[0 for i in xrange(target+1)] for j in xrange(target+1)]
    M[0] = [1 for i in xrange(target+1)]
    for i in xrange(1, target+1):
        for j in xrange(target+1):
            s = 0
            for c in coins:
                if c <= j:
                    s += M[i-c][c]
            M[i][j] = s

        #s = 0
        #for c in coins:
        #    if i - c >= 0:
        #        s += M[i-c]

    return M[target][target]

print answer(200)
