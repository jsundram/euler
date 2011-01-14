#!/usr/bin/env python
# encoding: utf-8
"""
100 - Choosing Disks.py

Created by Jason Sundram on 2010-09-23.
Copyright (c) 2010. All rights reserved.

Problem 100
15 July 2005

If a box contains 21 coloured discs, composed of 15 blue discs and 6 red discs, and 2 discs are taken at random,
it can be seen that the probability of taking two 2 discs, P(BB) = (15/21)(14/20) = 1/2.

The next such arrangement, for which there is exactly 50 percent chance of taking two blue discs at random, is a box containing 
85 blue discs and 35 red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
from timed import timed

@timed
def original_solution():
    """ original_solution took 0.024 ms
        The answer (original) is: 756872327473
    """
    
    # we know (b/n)*(b-1)/(n-1) = 1/2, so
    # 2b**2 - 2b - n**2 + n = 0
    # this is a quadratic diophantine equation
    # solve via http://www.alpertron.com.ar/METHODS.HTM (cheating?)
    b, n = 85, 120
    while n < 10**12:
      b, n = 3*b + 2*n - 2, 4*b + 3*n - 3
    return b

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

