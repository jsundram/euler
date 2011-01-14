#!/usr/bin/env python
# encoding: utf-8
"""
074 - Factorial Chains.py

Created by Jason Sundram on 2010-08-05.
Copyright (c) 2010. All rights reserved.

Problem 74
16 July 2004

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69  -> 363600 ->  1454 -> 169 -> 363601 -> ( 1454)
78  -> 45360  -> 871 ->  45361 -> ( 871)
540 -> 145 -> ( 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""
from timed import timed
from utils import combinations_with_replacement
import operator
from collections import defaultdict


def factorial(n):
    return reduce(operator.mul, xrange(2, n+1), 1)

def digfac_old(n):
    return reduce(operator.add, map(factorial, map(int, str(n))), 0)

# cache
fact = dict(zip(map(str, range(10)), (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)))
def digfac(n):
    s = 0
    for i in str(n):
        s += fact[i]
    return s

def fact_chain(n):
    s = set()
    # print n
    while n not in s:
        # print n
        s.add(n)
        n = digfac(n)
    # print "(%d)" % digfac(n)
    return len(s)

@timed
def original_solution_slow():
    "15min on mbp, sucky"
    N = 10**6
    count = 0
    for n in xrange(1, N+1):
        if fact_chain(n) == 60:
            print n
            count += 1
    return count

def num_permutations(l):
    """returns the number of permutations possible from iterable l."""
    counts = defaultdict(int)
    for i in l:
        counts[i] += 1
    
    # Can't have leading digit 0
    invalid = 0
    if 0 in counts:
        invalid = factorial(len(l) - 1)
    
    return factorial(len(l)) / reduce(operator.mul, map(factorial, counts.values()), 1) - invalid


@timed
def original_solution():
    """runtime on mbp is 1.026s"""
    count = 0
    for N in xrange(1, 7):
        for c in combinations_with_replacement(range(10), N):
            n = sum([i*10**n for (n, i) in zip(xrange(N), c)]) # convert tuple to int
            if fact_chain(n) == 60:
                print c
                count += num_permutations(c)
    return count

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

