#!/usr/bin/env python
# encoding: utf-8
"""
035 - Circular primes under 1 million.py

Created by Jason Sundram on 2009-12-03.

Problem 35
17 January 2003
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

import sys
import os

import math, time

def all_rots(l):
    yield l    
    n = len(l)
    for i in range(1, n):
        yield l[-i:] + l[:n-i]

def get_primes(upper_bound=1000000):
    """constructs a sieve and returns primes"""
    sieve = range(0, upper_bound)
    total = 0;
    sieve[1] = 0 # 1 is not prime
    for i in xrange(2, int(math.sqrt(upper_bound))):
        if (sieve[i] != 0):
            for j in xrange(2*i, upper_bound, i):
                sieve[j] = 0
    return [p for p in sieve if p != 0]


def digits(n):
    return map(int, list(str(n)))

def to_int(l):
    return int(''.join(map(str, l)))

def functional_solution():
    primes = set(get_primes)
    return [p for p in primes if all([to_int(x) in primes for x in all_rots(digits(p))])]
    
def main():
    start_time = time.time()
    
    primes = set(get_primes())
    circular = []
    
    for p in primes:
        d = digits(p)
        if all([to_int(x) in primes for x in all_rots(d)]):
            circular.append(p)
            print "found a circular prime: %d" % p

    print "Found %d circular primes" % len(circular)
    print "Elapsed Time: ", time.time() - start_time, "second(s)"


if __name__ == '__main__':
    main()
