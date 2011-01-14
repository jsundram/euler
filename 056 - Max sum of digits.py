#!/usr/bin/env python
# encoding: utf-8
"""
056 - Max sum of digits.py

Created by Jason Sundram on 2009-12-15.
Copyright (c) 2009. All rights reserved.

Problem 56
07 November 2003

A googol (10^(100)) is a massive number: one followed by one-hundred zeros; 
100^(100) is almost unimaginably large: one followed by two-hundred zeros. 

Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^(b), where a, b < 100, what is the maximum digital sum?
"""
from timed import timed

def digital_sum(n):
    """Returns the sum of the digits"""
    return sum(map(int, str(n)))
    
@timed
def original_solution():
    (m, A, B) = (0, 0, 0)
    for a in xrange(2, 100):
        for b in xrange(1, 100):
            e = digital_sum(a**b)
            if m < e:
                (m, A, B) = (e, a, b)
    
    print "%d ^ %d == %d" % (A, B, m)
    return m


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

