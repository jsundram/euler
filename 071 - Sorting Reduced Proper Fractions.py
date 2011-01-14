#!/usr/bin/env python
# encoding: utf-8
"""
071 - Sorting Reduced Proper Fractions.py

Created by Jason Sundram on 2010-08-02.
Copyright (c) 2010. All rights reserved.

Problem 71
04 June 2004

Consider the fraction, n/d, where n and d are positive integers. If n < d and n is relatively prime to d, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""
from timed import timed
from utils import gcd

@timed
def original_solution():
    """runtime on mbp is 93ms. 
        This is another case (I'm looking at you, #70) of decreasing runtime by looking
        where the answer is and returning. Searching the whole space takes considerably longer.
    """
    N = 1000*1000
    
    # from the data given, we know that we can do at least 2/5ths, use that as a starting point
    frac, best, three_sevenths = .4, 2, (3.0/7.0)
    
    for base in xrange(N, N-10, -1): # I bet we'll find it within 10 loops
        for n in xrange(int(frac*base), int(three_sevenths * base)):
            if frac < (float(n)/base) and gcd(n, base) == 1:
                best = n
                frac = float(n) / base
                #print "best: (%d / %d) " % (n, base)
    
    return best


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

