#!/usr/bin/env python

def get_triangle_array(filename):
    nums = list()
    with open(filename) as f:
        for line in f:
            nums.append([int(num) for num in line.split()])

    return nums

def combine_lines(arr):
    # arr is a lower triangle array
    for i in range(len(arr)-1):
        max_num = max(arr[-1][i], arr[-1][i+1])
        arr[-2][i] += max_num

    del arr[-1]
    return arr

if __name__ == "__main__":
    arr = get_triangle_array("Problem018_input.txt")
    while len(arr) > 1:
        arr = combine_lines(arr)

    print arr[0][0]
