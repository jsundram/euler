#!/usr/bin/env python
# encoding: utf-8
"""
075 - Wire Triangles.py

Created by Jason Sundram on 2010-08-06.
Copyright (c) 2010. All rights reserved.

Problem 75
30 July 2004

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer-sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
"""
from timed import timed
from utils import gcd, get_primes
from collections import defaultdict

@timed
def original_solution():
    """ original_solution took 2711.536 ms
        The answer (original) is: 161667
    """
    N = 1500*1000 
    sqrt_N = int(N**.5) + 1
    wires = defaultdict(int)
    # So, we're looking for all pythagorean triplets that sum to less than 1.5M
    # use Euclid's formula: http://en.wikipedia.org/wiki/Pythagorean_triple
    for m in xrange(1, sqrt_N):
        for n in xrange(1, m):
            if gcd(n, m) == 1 and (m+n)%2 == 1: # primitive
                sides = m**2 - n**2, 2*m*n, m**2 + n**2
                perimeter = sum(sides)
                #print "(%d, %d): %s -> %d" % (m, n, sides, perimeter)
                for p in xrange(perimeter, N+1, perimeter):
                    #print '\t', p
                    wires[p] += 1
    
    count = 0
    for p, n in wires.iteritems():
        if n == 1:
            count += 1
    return count

@timed
def optimized_solution():
    """optimized_solution took 638.455 ms"""
    N = 1500*1000 
    sqrt_N = int(N**.5) + 1
    wires = [0] * (N+1) # array = hash for ints. This saves about a second.
    
    for m in xrange(1, sqrt_N):
        start = 2 if (m & 1) else 1 # if m is even, n is odd, and vice versa
        end = min(m, 1 + int(N / 2.0 / m) - m) # choose the end so that the max perimeter is <= N
        for n in xrange(start, end, 2):
            if gcd(n, m) == 1: # primitive
                perimeter = 2*m*(m + n)
                for p in xrange(perimeter, N+1, perimeter):
                    wires[p] += 1
    
    return wires.count(1)
    
def main():
    print 'The answer (original) is: %d' % optimized_solution()


if __name__ == '__main__':
    main()

