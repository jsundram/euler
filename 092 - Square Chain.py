#!/usr/bin/env python
# encoding: utf-8
"""
092 - Square Chain.py

Created by Jason Sundram on 2010-08-06.
Copyright (c) 2010. All rights reserved.

Problem 92
01 April 2005

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
from timed import timed
from utils import combinations_with_replacement, factorial
import operator
from collections import defaultdict
import psyco; psyco.full()

def get_next(n):
    return sum([int(i)*int(i) for i in str(n)])

def num_permutations(l):
    """returns the number of permutations possible from iterable l. Copied from 74, with fixes"""
    counts = defaultdict(int)
    for i in l:
        counts[i] += 1
    
    # Can't have leading digit 0
    invalid = 0
    if 0 in counts:
        n = list(l)
        n.remove(0) # just get rid of one
        invalid = num_permutations(['A' if i == 0 else i for i in n])
    
    return factorial(len(l)) / reduce(operator.mul, map(factorial, counts.values()), 1) - invalid

@timed
def faster():
    """765ms"""
    table = {0:0, 1:1, 89:89}
    for i in xrange(2, 600):
        n = i
        while i != 1 and i != 89:
            i = get_next(i)
        table[n] = i
    
    T = {}
    count = 0
    for i in xrange(1, 8):
        for c in combinations_with_replacement(range(10), i):
            s = ''.join(map(str, sorted(c)))
            n = get_next(int(s))
            if table[n] == 89:
                count += num_permutations(c)
    return count

@timed
def original_solution():
    """ original_solution took 7846.661 ms (yikes, but first try took 60s)
        The answer (original) is: 8581146
    """
    table = {1:1, 89:89}
    for i in xrange(2, 600):
        n = i
        while i != 1 and i != 89:
            i = get_next(i)
        table[n] = i
    
    N = 10**7
    count = 0
    pows = dict([(str(i), i*i) for i in xrange(10)])
    for n in xrange(2, N):
        next = 0
        for i in str(n):
             next += pows[i]
        
        if table[next] == 89:
            count += 1
    return count


def main():
    print 'The answer (original) is: %d' % faster()


if __name__ == '__main__':
    main()

