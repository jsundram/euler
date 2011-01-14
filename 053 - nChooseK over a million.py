#!/usr/bin/env python
# encoding: utf-8
"""
053 - nChooseK over a million.py

Created by Jason Sundram on 2009-12-10.
Copyright (c) 2009. All rights reserved.

Problem 53
26 September 2003

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5, 3) = 10.

In general,
C(n, r) = n! / (r!(n−r)!) where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: C(23, 10) = 1144066.

How many, not necessarily distinct, values of C(n,r) for 1 ≤ n ≤ 100, are greater than one-million?

"""
from timed import timed
import operator


@timed
def original_solution():
    f = lambda x : reduce(operator.mul, range(1, x+1, 1)) # default arg to reduce, courtesy of LKA
    C = lambda n,r : f(n) / (f(r) * f(n-r))
    
    N = 1000 * 1000
    n_max = 100
    count = 0
    # Could be smart and use the symmetric nature of C(n,r) and the fact that it's ascending to do this faster. 
    # But this is fast enough.
    for n in xrange(1,n_max + 1):
        for r in xrange(1, n/2): 
            if N < C(n,r):
                count += 2
        if N < C(n, n/2): 
            count += 1 if n % 2 == 0 else 2
    return count


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

