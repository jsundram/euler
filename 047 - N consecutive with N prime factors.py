#!/usr/bin/env python
# encoding: utf-8
"""
047 - N consecutive with N prime factors.py

Created by Jason Sundram on 2009-12-07.
Copyright (c) 2009. All rights reserved.

Problem 47
04 July 2003

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
"""
from timed import timed


def consecutive(n):
    # kinda like a sieve.
    N = 1000000
    sieve = [0] * N
    count = 0
    for i in xrange(2, N):
        if sieve[i] == 0:
            # prime. reset count, update sieve
            count = 0 
            for k in xrange(2*i, N, i): sieve[k] += 1
        elif sieve[i] == n:
            count +=1
            if count == n:
                return i-n+1
        else:
            count = 0
    return -1

@timed
def original_solution():
    return consecutive(4)


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

