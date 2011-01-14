#!/usr/bin/env python
# encoding: utf-8
"""
052 - Multiples with Same Digits.py

Created by Jason Sundram on 2009-12-10.
Copyright (c) 2009. All rights reserved.

Problem 52
12 September 2003

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
from timed import timed

@timed
def original_solution():
    N = 1000*1000
    
    for i in xrange(1,N):
        s = set(str(i))
        mul = lambda x : i*x
        test = lambda x : set(str(x)) == s
        if all(test(j) for j in map(mul, range(2,7))):
            return i
    return -1

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    try:
        import psyco #;psyco.full()
        #psyco.bind(original_solution)
    except ImportError:
        pass
    main()