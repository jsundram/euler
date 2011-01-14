#!/usr/bin/env python
# encoding: utf-8
"""
072 - Cardinality of Reduce Fraction Set.py

Created by Jason Sundram on 2010-08-03.
Copyright (c) 2010. All rights reserved.

Problem 72
18 June 2004

Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
"""
from timed import timed
from utils import get_primes
import operator

N = 1000*1000


def farey_length(n): 
    """From the encyclopedia of integer sequences:
        a(n) = n(n+3)/2 - sum(a([n/k]) for k in xrange(2, n)). - David W. Wilson, May 25, 2002
        This is actually quite slow . . .
    """
    return n*(n+3)/2 - sum(a(n/k) for k in xrange(2,n))


@timed
def make_factored_list(n):
    # make a list of lists
    d = []
    for i in xrange(n+1):
        d.append([])
    
    end = 1 + (n/2)
    for i in xrange(2, end):
        if not d[i]:
            for j in xrange(i*2, n+1, i):
                d[j].append(i)
    
    # for i, l in enumerate(d): print "%d: %s" % (i, l)
    return d

def do_phi(n, prime_factors):
    """Can calculate phi(n) really fast if we know n's prime_factors!"""
    if prime_factors:
        return int(reduce(operator.mul, [n] + [(1.0 - (1.0 / p)) for p in prime_factors]))
    return n-1


@timed
def original_solution():
    """runtime on mbp: 6.055s, yikes.
       could just build a phi list instead of a factor list ... but that would still be about 2 seconds  """
    # want sequence length: http://en.wikipedia.org/wiki/Farey_sequence#Sequence_length
    # we know the answer is roughly 3n**2 / pi**2
    # answer is exactly: sum of phi(n) for n in range [1, N]
    l = make_factored_list(N) # 2 seconds ...
    s = 1
    for n in xrange(len(l)):
        s += do_phi(n, l[n])
        
    
    return s

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

