#!/usr/bin/env python
# encoding: utf-8
"""
058 - Primes on Square Spirals.py

Created by Jason Sundram on 2009-12-17.
Copyright (c) 2009. All rights reserved.

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

"""
from timed import timed
import utils


@timed
def original_solution():
    """4 seconds or so. Was going to make this faster with a search, but function is iterative."""
    prime_count = 0
    j = 3
    while True:
        for i in (1, 2, 3):
            prime_count += utils.is_prime_MR( j*j - i*(j - 1))
        
        if prime_count * 10 < j*2 - 1: 
            return  j
        
        j += 2


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

