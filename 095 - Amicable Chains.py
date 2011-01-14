#!/usr/bin/env python
# encoding: utf-8
"""
095 - Amicable Chains.py

Created by Jason Sundram on 2010-09-22.
Copyright (c) 2010. All rights reserved.

Problem 95
13 May 2005

The proper divisors of a number are all the divisors excluding the number itself. 
For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. 
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496  14288  15472  14536  14264 ( 12496  ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""
from timed import timed
from utils import proper_divisors, memoized, is_prime

N = 10**6

@timed
def tzaman(lim):
    """from the forums, used a sieve. 5400.281 ms"""
    div = [0]*lim # Sieving for divisor sums.
    for i in xrange(1, lim):
        for j in xrange(2*i, lim, i):
            div[j] += i
    
    chain = [0]*lim # Chains: -1 = bad, 0 = untested, n = length of chain
    chain[0] = -1
    for i in xrange(1, lim):
        if chain[i]: continue
        seq = [i]
        while div[seq[-1]] < lim and chain[div[seq[-1]]] == 0 and div[seq[-1]] not in seq:
            seq.append(div[seq[-1]])
        if div[seq[-1]] in seq: # We hit a loop
            loop = seq.index(div[seq[-1]])
            for l in range(0, loop):
                chain[seq[l]] = -1 # pre-loop: mark as bad
            for l in range(loop, len(seq)):
                chain[seq[l]] = len(seq)-loop # within-loop: mark chain length
        else: # Exceeded lim or hit a bad number.
            for s in seq: chain[s] = -1 # mark as bad
    return chain.index(max(chain))

@memoized
def divisor_sum(n):
    return sum(proper_divisors(n))

def get_chain(i):
    global N
    chain = set([1, i])
    next = divisor_sum(i)
    while next < N and next not in chain:
        chain.add(next)
        next = divisor_sum(next)
    if next == i:
        chain.remove(1)
        return chain
        
    return []

@timed
def original_solution():
    """ original_solution took 3077.738 ms (with cheat by stopping early)
        original_solution took 372,081.497 ms (over 6 minutes to look at everything!)
        The answer (original) is: 14316
    """
    min_element, max_length = 0, 1
    stop = N/50# N # cheat here and stop early
    for i in xrange(1, stop): 
        if i % 10000 == 0: print i
        c = get_chain(i)
        if max_length < len(c):
            min_element, max_length = min(c), len(c)
            print i, min_element, max_length
    
    return min_element

# could use google:
# http://amicable.homepage.dk/knwncx.htm gives the answer here:
# http://amicable.adsl.dk/aliquot/cx/c28.txt
# and there are no known amicable chains with 4 elements under a million:
# http://amicable.homepage.dk/knwnc4.htm
# These sequences are also known as aliquot sequences: http://en.wikipedia.org/wiki/Aliquot_sequence
def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

