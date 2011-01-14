#!/usr/bin/env python
# encoding: utf-8
"""
069 - Maximize Totient.py

Created by Jason Sundram on 2010-06-16.
Copyright (c) 2010. All rights reserved.

Problem 69
07 May 2004

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n   Relatively Prime    φ(n)    n / φ(n)
2   1                   1       2
3   1,2                 2       1.5
4   1,3                 2       2
5   1,2,3,4             4       1.25
6   1,5                 2       3
7   1,2,3,4,5,6         6       1.1666...
8   1,3,5,7             4       2
9   1,2,4,5,7,8         6       1.5
10  1,3,7,9             4       2.5
It can be seen that n=6 produces a maximum n/φ(n) for n  10.

Find the value of n <= 1,000,000 for which n/φ(n) is a maximum.
"""
import math
from timed import timed
from utils import get_primes


@timed
def original_solution():
    """Some insight here: we're basically looking for the largest product of unique primes less than N
       How many primes do we need to look at?
       1M = 10^6 = (2*5)^6, so we need at most 12 primes, so we can stop at 19.
       
       runtime on mbp is 0.040ms (< 1ms!!!)
    """
    N = 1000 * 1000
    
    product = 1
    for p in get_primes(19):
        product *= p
        if N < product:
            return product / p
    return None


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

