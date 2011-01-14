#!/usr/bin/env python
# encoding: utf-8
"""
070 - Permute Totient.py

Created by Jason Sundram on 2010-06-16.
Copyright (c) 2010. All rights reserved.

Problem 70
21 May 2004

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""
from timed import timed
from utils import get_primes
import operator

N = 10**7

def phi(n):
    """ returns Euler's Totient of n (all the number less than n that are coprime with n)"""
    # assumes you have a primelist, primelist = set(primes). otherwise stop at n, not half, below.
    if n in primelist: return n-1
    
    res = n
    half = 1 + n / 2
    for p in primes:
        if half < p:
            break;
        elif n % p == 0:
            res *= (1.0 - (1.0 / p))
    
    return int(res)

def digits(n):
    xrange()
    while n != 0:
       q, r = divmod(n, 10)
       d.append(r)
       n = q
    return d

def permutes(m, n):
    """ returns true if m and n are permutations of each other. faster than the O(n) defaultdict approach"""
    #return not any(i!=j for (i,j) in zip(sorted(list(str(m))), sorted(list(str(n)))))
    lm = list(str(m))
    ln = list(str(n))
    if set(lm) != set(ln):
        return False
    # else
    for (i,j) in zip(sorted(lm), sorted(ln)):
        if i != j:
            return False
    return True

def do_phi(n, prime_factors):
    """Can calculate phi(n) really fast if we know n's prime_factors!"""
    return int(reduce(operator.mul, [n] + [(1.0 - (1.0 / p)) for p in prime_factors]))

@timed
def fcomposites(n, N=10**7):
    """ Returns composites that are the product of 2 distinct prime factors, less than N, and their factors
        This takes about a minute for N=10**7.
    """
    # make a sieve that lists the prime factors of each number in it.
    primes = get_primes(N)
    sieve = [[] for i in xrange(N)]
    for i in xrange(2, N):
        if len(sieve[i]) == 0:
            # prime. update sieve
            for k in xrange(2*i, N, i):
                sieve[k].append(i)
    return ((i, sieve[i]) for i in xrange(2, N) if len(sieve[i]) == n)

# could speed this up by generating composites via multiplication instead of sieve-reduce, and using the identity
# phi(p*q) = (p-1)(q-1)
# might not need as many primes as we generate, either.
@timed
def original_solution():
    """runtime on mbp is 128 seconds. Answer: 8319823 (=2339*3557)"""
    # http://mathworld.wolfram.com/TotientFunction.html
    # phi(n) is even for n > 3
    # if a,b coprime and a,c coprime, then a,bc coprime
    
    # if any prime had this property, it would be maximal, but no prime can, since 
    # p and p-1 can't be permutations of each other, since they differ in only one place
    # what about numbers with only 2 prime factors, or a power of a prime?
    candidates = {} # store a map of n/phi(n) -> n
    for i, f in fcomposites(2, N):
        p = do_phi(i, f)
        newphi = ((f[0]-1) * (f[1] -1))
        if permutes(i, p):
            print "phi(%d) = %d" % (i, p)
            candidates[float(i) / p] = i
    f = min(candidates)
    return candidates[f]

def fc(N, radius):
    """Generate composites with 2 prime factors less than N, with primes within given radius of sqrt(N)"""
    s = N**.5
    pmin, pmax = (s - radius, s + radius)
    p = filter(lambda x : pmin < x, get_primes(int(pmax)))
    # partition into two groups to avoid looking at both i*j and j*i
    l = [i for i in p if i < s]
    h = [i for i in p if s < i]
    return ((i*j, [i,j]) for i in l for j in h if (i*j) <= N)

@timed
def faster():
    """runtime on mbp is 350ms"""
    # choose search radius proportional to sqrt(N). Half sounds good, since we want primes close to sqrt(N)
    fcomposites = fc(N, .5*N**.5)
    candidates = {} # store a map of n/phi(n) -> n
    n = 0
    for i, f in fcomposites:
        n +=1
        p = do_phi(i, f)
        if permutes(i, p):
            #print "phi(%d) = %d [factors are %s]" % (i, p, f)
            candidates[float(i) / p] = i
    print "examined %d composites" % (n)
    
    f = min(candidates)
    return candidates[f]
    
def main():
    print 'The answer (original) is: %d' % faster()


if __name__ == '__main__':
    main()

