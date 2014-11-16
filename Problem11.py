#!/usr/bin/env python

#TODO make this cleaner

def build_arr(filename):
    arr = []
    f = open(filename)
    for line in f:
        nums = [int(n) for n in line.split()]
        arr.append(nums)

    return arr

def left_diag_product(start, arr):
    x, y = start
    n1 = arr[x][y]
    n2 = arr[x-1][y+1]
    n3 = arr[x-2][y+2]
    n4 = arr[x-3][y+3]
    return n1 * n2 * n3 * n4

def right_diag_product(start, arr):
    x, y = start
    n1 = arr[x][y]
    n2 = arr[x+1][y+1]
    n3 = arr[x+2][y+2]
    n4 = arr[x+3][y+3]
    return n1 * n2 * n3 * n4

def down_product(start, arr):
    x, y = start
    n1 = arr[x][y]
    n2 = arr[x][y+1]
    n3 = arr[x][y+2]
    n4 = arr[x][y+3]
    return n1 * n2 * n3 * n4

def right_product(start, arr):
    x, y = start
    n1 = arr[x][y]
    n2 = arr[x+1][y]
    n3 = arr[x+2][y]
    n4 = arr[x+3][y]
    return n1 * n2 * n3 * n4

if __name__ == "__main__":
    max_product = 0
    arr = build_arr("Problem11_input.txt")
    # Find right diag products
    for i in range(len(arr)-3):
        for j in range(len(arr[i]) - 3):
            prod = right_diag_product((j, i), arr)
            if prod > max_product:
                max_product = prod

    # Find left diag products
    for i in range(len(arr)-3):
        for j in range(3, len(arr[i])):
            prod = left_diag_product((j, i), arr)
            if prod > max_product:
                max_product = prod

    # Find down products
    for i in range(len(arr)-3):
        for j in range(len(arr)):
            prod = down_product((j, i), arr)
            if prod > max_product:
                max_product = prod

    # Find right products
    for i in range(len(arr)):
        for j in range(len(arr) - 3):
            prod = right_product((j, i), arr)
            if prod > max_product:
                max_product = prod

    print max_product
