#!/usr/bin/env python
# encoding: utf-8
"""
046 - Goldbach Conjecture.py

Created by Jason Sundram on 2009-12-07.
Copyright (c) 2009. All rights reserved.

Problem 46
20 June 2003

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^(2)
15 = 7 + 2×2^(2)
21 = 3 + 2×3^(2)
25 = 7 + 2×3^(2)
27 = 19 + 2×2^(2)
33 = 31 + 2×1^(2)

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""
from timed import timed

@timed
def get_primes(N=1000000):
    """Faster primes, courtesy of LKA"""
    sqrt_N = 1 + int(N**.5)
    sieve = set(xrange(2,N))
    
    for i in xrange(2, sqrt_N):
        if (i in sieve):
            sieve.difference_update(xrange(i*i, N, i))
    return sieve

primes = get_primes()

def perfect_square(n):
    r = int(n **.5)
    return r*r == n

def goldbach(n):
    g = lambda x : perfect_square(x/2)
    for p in primes:
        if p > n: return False
        if g(n - p): return True

@timed
def original_solution():
    N = 1000000
    for i in xrange(3, N, 2):
        if i not in primes and not goldbach(i):
            return i
    return -1

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

