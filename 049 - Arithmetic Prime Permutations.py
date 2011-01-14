#!/usr/bin/env python
# encoding: utf-8
"""
049 - Arithmetic Prime Permutations.py

Created by Jason Sundram on 2009-12-08.
Copyright (c) 2009. All rights reserved.

Problem 49
01 August 2003

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
    (i)  each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

primes = get_primes(10000) # 4 digit primes
primes = [p for p in primes if 1000 < p]


def has_arithmetic_sequence(l):
    """Does there exist some n such that l_i + n = l_j, and l_j + n = l_k, for l_i, l_j, and l_k in l?"""
    
    def subsets(l, length):
        """Returns a list of all subsets of len length"""
        subsets = []
        n = len(l)
        N = 2**len(l)
        for i in xrange(0, N):
            sub = [l[j] for j in xrange(0, n) if (i >> j & 1)]
            if length == len(sub):
                subsets.append(sub)
        return subsets
    
    # generate all lists of length 3
    for s in subsets(l, 3):
        if is_arithmetic_sequence(s):
            return s
    return []
    
def is_arithmetic_sequence(l):
    """is the 3-element sequence arithmetic?"""
    def adjacent_difference(l):
        return [l[i+1] - l[i] for i in xrange(len(l)-1)]
    
    d = adjacent_difference(l)
    return d[0] == d[1]

@timed
def original_solution():
    visited = set()
    digits = lambda n: set(map(int, str(n)))
    def permutations(p):
        """Returns a list of the permutations of the digits of p that are prime."""
        d = digits(p)
        return [x for x in primes if digits(x) == d]
    
    for p in primes:
        if p in visited:
            continue
        perms = permutations(p)
        visited.update(set(perms))
        if len(perms) < 3: 
            continue
        s = has_arithmetic_sequence(perms)
        if len(s) != 0 and s != [1487,4817,8147]:
            print s
            return int(''.join(map(str, s)))
    return -1

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

