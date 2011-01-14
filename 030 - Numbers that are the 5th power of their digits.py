#!/usr/bin/env python
# encoding: utf-8
"""
030 - Numbers that are the 5th power of their digits.py

Created by Jason Sundram on 2009-11-08.

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

import sys
import os


def fifth_power_of_digits(n):
    "Returns the sum of the fifth power of each of the digits in n. e.g. 12 -> 1^5 + 2^5 = 33"
    s = 0
    while 0 < n:
        s += (n % 10) ** 5
        n = n / 10
    return s

def original_solution():
    s = 0
    # Reasoning behind end bound: 
    # At a certain point, adding n^5 won't help you, i.e. n^5 + x < n * (log10(x) + 1)
    # log10(9**5) < 5.    
    for n in xrange(10, 10**6):
        if n == fifth_power_of_digits(n):
            s += n
            print "Found one: %d" % n
    print "Sum: %d" % s

def functional_solution():
    start = 10 
    end = 10 ** 6
    
    digits = lambda n: [int(c) for c in str(n)] # map(int, list(str(n)))
    sum5thpower = lambda n:sum(map(lambda x:x**5, digits(n)))
    print sum([n for n in xrange(start, end) if n == sum5thpower(n)])

def main():
    return functional_solution()
    
if __name__ == '__main__':
    main()

