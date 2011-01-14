#!/usr/bin/env python
# encoding: utf-8
"""
077 - Integers expressed as prime sums.py

Created by Jason Sundram on 2010-08-11.
Copyright (c) 2010. All rights reserved.

Problem 77
27 August 2004

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

2,3,5,7

9:
7 + 2
5 + 2 + 2
3 + 3 + 3
2 + 2 + 2 + 3

8:
5 + 3
3 + 3 + 2
2 + 2 + 2 + 2


What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
from timed import timed
from utils import get_primes, memoized

@memoized
def getp(n):
    return sorted(get_primes(n), reverse=True)

@memoized # I program DYNAMICALLY.
def _ways(x, maxP):
    "Recursive."
    if x == 0:
        return 1
    ways = 0
    for p in getp(min(x, maxP)):
        ways += _ways(x - p, p)
    return ways

def ways(x):
    return _ways(x, x)


def binary_search(lo, hi, compare):
    """compare is a cmp-like function"""
    mid = (hi + lo) / 2
    while hi - lo > 1:
        mid = (hi + lo) / 2
        v = compare(mid)
        if 0 < v:
            hi = mid
        elif v < 0:
            lo = mid
        else:
            return mid
    
    return lo if 0 < compare(mid) else hi


@timed
def original_solution():
    """ This is just like 31, right? Although 45, 46, 47 are all wrong
        original_solution took 1387.244 ms (without memoization)
        original_solution took 8.280 ms (with memoize)
        The answer (original) is: 71
    """
    N = 5000
    x = 10
    while ways(x) < N:
        x *= 2
    
    x = binary_search(x/2, x, lambda x : cmp(ways(x), N))
    return x + 1


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

