#!/usr/bin/env python
# encoding: utf-8
"""
050 - Prime from Consecutive Prime Sum.py

Created by Jason Sundram on 2009-12-08.
Copyright (c) 2009. All rights reserved.

Problem 50
15 August 2003

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
from timed import timed

@timed
def primes(N=1000000):
    """Fastest primes yet, bool sieve with range assignment."""
    sqrt_N = 1 + int(N**.5)
    sieve = [True] * (N + 1)
    sieve[0] = False; sieve[1] = False
    
    for i in xrange(2, sqrt_N):
        if sieve[i]:
            m = N / i - i
            sieve[i*i:N+1:i] = [False] * (m + 1)
    
    return [i for i in xrange(N+1) if sieve[i]]

# Globals
N = 1000000
primes = primes(1000000) 

_primesum = [0] * len(primes)
for (i,p) in enumerate(primes):
    _primesum[i] = p + _primesum[i-1]
_primesum = [0] + _primesum

def is_prime(n):
    return n in primes

def primesum(i, j):
    """returns sum for prime_i through prime_j"""
    return _primesum[j] - _primesum[i]

def binary_search(l, x):
    """searches l for x, returns (-1, mid) if not found"""
    low = 0
    high = len(l)
    
    while low <= high:
        mid = (low + high) / 2
        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1;
        else:
            return mid;
    return (-1, mid)


@timed
def original_solution():
    (m, mp) = (0, 0)
    (k, upper_bound) = binary_search(_primesum, N)
    for i in xrange(upper_bound):
        for j in xrange(upper_bound, i + m, -1):
            if m < (j - i):
                s = primesum(i, j)
                if s in primes: 
                    mp = s
                    m = j - i
    return mp


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

