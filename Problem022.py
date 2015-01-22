#!/usr/bin/env python

def sum_of_letters(name):
    tot = 0
    for ch in name:
        tot += ord(ch) - ord('A') + 1

    return tot

def score(name, idx):
    return sum_of_letters(name) * idx

def extract_names(filename):
    with open(filename) as f:
        for line in f:
            l = line.split(',')

        l = [s.translate(None, '"').upper() for s in l]

    return sorted(l)

if __name__ == "__main__":
    names = extract_names("Problem022_input.txt")
    tot = 0
    for i, name in enumerate(names):
        tot += score(name, i+1)

    print tot
