#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Jason Sundram on 2009-09-23.
Copyright (c) 2009 The Echo Nest. All rights reserved.


A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

import sys
import os
import time

def stringify(l):
    return ''.join(map(str, l))

# from here: http://docs.python.org/library/itertools.html#itertools.permutations
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def main():
    start = time.time()
    for (n, permutation) in enumerate(permutations(range(10))):
        if (n + 1) == 1000000:
            print stringify(permutation)
            break
    duration = time.time() - start
    print "found answer in %2.3f seconds" % duration

if __name__ == '__main__':
    main()

