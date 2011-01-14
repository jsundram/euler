#!/usr/bin/env python
# encoding: utf-8
"""
051 - Prime Value Families.py

Created by Jason Sundram on 2009-12-08.
Copyright (c) 2009. All rights reserved.

Problem 51
29 August 2003

By replacing the 1st digit of *3, it turns out that six of the nine possible values: 
    13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number 
is the first example having seven primes among the ten generated numbers, yielding the family: 
56003, 56113, 56333, 56443, 56663, 56773, and 56993. 

Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.
"""

from timed import timed, loop_timer
from utils import get_primes

primes = get_primes()
digits = map(str, range(10))

def prime_family_size(p):
    sp = str(p)
    m = 0
    for c in set(str(p/10)): # ignore lowest digit, since only 1,3,7,9 are valid values
        if sp.count(c) < 2: continue
        l = 0
        for d in digits:
            q = sp.replace(c, d)
            if int(q) in primes and q[0] != '0': # leading 0 doesn't count (e.g. 03)
                # print q
                l += 1
        if m < l:
            m = l
            #print "max %d yielded by replacing %s" % (m, c)
            
    return m
    
def candidate(s):
    """Only look at primes with at least 3 repititions"""
    return len(s) - len(set(s)) > 2 
    
@timed
def original_solution():
    """Could shave a few seconds off by starting at 56003, which was given to us."""
    m = 0
    for p in primes:#loop_timer(primes):
        s = str(p)
        if  candidate(s) and m < prime_family_size(p):
            m = prime_family_size(p)
            print "%d has prime family size %d" % (p, m)
            if m == 8: return p
    
    return -1


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    """    try:
            import psyco
            #psyco.full()
            # psyco.bind(prime_family_size)
        except ImportError:
            pass
    """    
    main()

