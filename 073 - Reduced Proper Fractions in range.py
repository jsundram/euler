#!/usr/bin/env python
# encoding: utf-8
"""
073 - Reduced Proper Fractions in range.py

Created by Jason Sundram on 2010-08-05.
Copyright (c) 2010. All rights reserved.

Problem 73
02 July 2004

Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?

Note: The upper limit has been changed recently.
"""
from timed import timed
from utils import gcd, get_primes

@timed
def original_solution():
    """runtime on mbp is: 31s, yikes. Solution based on #71
        Want to just take 1/3 of the sequence length (calculated using #72), which is really close, but off by 4
    """
    N = 12000
    # from the data given, we know that we can do at least 2/5ths, use that as a starting point
    start, end = (1.0/3.0), (1.0/2.0)
    count = 0
    for base in xrange(1, N+1):
        for n in xrange(int(start*base), int(end * base)+1):
            if start < (float(n) / base) < end and gcd(n, base) == 1:
                count += 1
    return count

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

