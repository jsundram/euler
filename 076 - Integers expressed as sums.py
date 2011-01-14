#!/usr/bin/env python
# encoding: utf-8
"""
076 - Integers expressed as sums.py

Created by Jason Sundram on 2010-08-06.
Copyright (c) 2010. All rights reserved.

Problem 76
13 August 2004

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
from timed import timed
from utils import memoized

@memoized # Dynamic Programming FTW
def p(k, n):
    if k > n:
        return 0
    if k == n:
        return 1
    return p(k+1, n) + p(k, n-k)

def partition(n):
    """http://en.wikipedia.org/wiki/Partition_(number_theory)"""
    s = 0 # need to subtract one for our purposes, since n + 0 doesn't count.
    for k in xrange(1, 1 + n/2):
        s += p(k, n-k)
    return s


@timed
def original_solution():
    """ original_solution took 38.313 ms
        The answer (original) is: 190569291
    """
    N = 100
    return partition(N)


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

