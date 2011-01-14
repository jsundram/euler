#!/usr/bin/env python
# encoding: utf-8
"""
039 - Triangles with Perimeter.py

Created by Jason Sundram on 2009-12-04.

projecteuler.net logo
Problem 39
14 March 2003

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""

from timed import timed # helper for timing.
from collections import defaultdict

def next_triangle(N,M,K):
    """Generates pythagorean triangles (not uniquely) using formula from wikipedia."""
    for n in xrange(1, N):
        for m in xrange(n, M):
            for k in xrange(1, K):
                a = k * (m*m - n*n)
                b = k * (2 * m * n)
                c = k * (m*m + n*n)
                yield (a,b,c)


def list_hash(l):
    """Python won't hash lists for us, but it's real easy to do. Probably not great for large lists."""
    l.sort()
    return str(l)


@timed
def original_solution():
    perimeters = defaultdict(int)
    seen = set()
    for (a,b,c) in next_triangle(23, 23, 500): # no side can be bigger than 500 to have perimeter < 1000
        p = a + b + c
        if 0 < a and 0 < b and 0 < c and p <= 1000:
            s = list_hash([a,b,c])
            
            if s not in seen:
                perimeters[p] += 1
                seen.add(s)
    
    (p, times) = max(perimeters.iteritems(), key=lambda (k,v):v)
    print "Perimeter %d occurred %d times" % (p, times)
    return p


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

