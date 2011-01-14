#!/usr/bin/env python
# encoding: utf-8
"""
060 - Concatenating Primes.py

Created by Jason Sundram on 2009-12-19.
Copyright (c) 2009. All rights reserved.

Problem 60
02 January 2004

The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from math import log10
from timed import timed
import utils
from collections import defaultdict

LIMIT = 9000 # just a guess
all_primes = utils.get_primes(LIMIT)
# minor optimization
all_primes.remove(2)
all_primes.remove(5)

def is_prime(n):
    if n < LIMIT: 
        return n in all_primes

    return utils.is_prime(n)


def test(i, j):
    # f = lambda x, y : int(str(x) + str(y)) # get a 1-second speedup by doing this with math
    order = lambda x : 10**(1 + int(log10(x)))
    f = lambda x, y : x * order(y) + y
    
    return is_prime(f(i, j)) and is_prime(f(j, i))

@utils.memoized # dynamic programming FTW
def clique(p, l=all_primes):
    """Returns all friends of p greater than p"""
    return set([i for i in l if p < i and test(i, p)])

def cutsort(l, n):
    """returns all items in l with values greater than n in a set"""
    return set([i for i in l if n < i])

@timed
def original_solution(l=all_primes, N=5):
    """Runtime on mbp is 14.5 seconds"""
    # The & notation for set intersection is handy here.
    for p1 in l:
        for p2 in sorted(clique(p1)):
            i1 = cutsort(clique(p1) & clique(p2), p2)
            for p3 in i1:
                i2 = cutsort(i1 & clique(p3), p3)
                for p4 in i2:
                    i3 =  cutsort(i2 & clique(p4), p4)
                    for p5 in i3:
                        c = (p1, p2, p3, p4, p5)
                        print c
                        return sum(c)
    
    print "found nothing"
    return -1


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

