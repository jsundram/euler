#!/usr/bin/env python
# encoding: utf-8
"""
087 - Summing Prime Powers.py

Created by Jason Sundram on 2010-08-06.
Copyright (c) 2010. All rights reserved.

Problem 87
21 January 2005

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""
from timed import timed
from utils import get_primes, product
from bisect import bisect

# import psyco; psyco.full() gets the time down to 430 ms
@timed
def original_solution():
    """ original_solution took 731.178 ms
        The answer (original) is: 1097343
    """
    N = 50*10**6
    squares = [p**2 for p in get_primes(int(N**(1.0/2.0)) + 1)]
    cubes   = [p**3 for p in get_primes(int(N**(1.0/3.0)) + 1)]
    fourths = [p**4 for p in get_primes(int(N**(1.0/4.0)) + 1)]
    
    # Some numbers can be expressed as the sum of prime powers in two different ways.
    # I'm looking at you, 145 = 121 + 8 + 16 = 4 + 125 + 16.
    numbers = set()
    S, C = 0, 0 
    for f in fourths:
        b = N - f
        C = bisect(cubes, b)
        for c in cubes[:C]:
            S = bisect(squares, b - c)
            for s in squares[:S]:
                numbers.add(f + c + s)
    
    return len(numbers)


def main():
    
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

