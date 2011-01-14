#!/usr/bin/env python
# encoding: utf-8
"""
080 - Square Roots.py

Created by Jason Sundram on 2010-08-25.
Copyright (c) 2010. All rights reserved.

Problem 80
08 October 2004

It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
from timed import timed
from utils import is_perfect_square as psq

from decimal import Decimal, getcontext
getcontext().prec = 110 # breathing room

def golfed():
    return sum(map(lambda n : 0 if psq(n) else sum(map(int, str(Decimal(n).sqrt()).replace('.', '')[:100])), xrange(101)))

def sqrt_sum(n):
    if psq(n):
        return 0
    
    s = str(Decimal(n).sqrt()).replace('.', '')[:100]
    return sum(map(int, s))


@timed
def original_solution():
    """ original_solution took 673.908 ms
        The answer (original) is: 40886
    """
    N = 100
    return sum(map(sqrt_sum, xrange(N+1)))


def main():
    print 'The answer (original) is: %d' % original_solution()
    print golfed()

if __name__ == '__main__':
    main()

