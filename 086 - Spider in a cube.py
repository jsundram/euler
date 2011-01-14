#!/usr/bin/env python
# encoding: utf-8
"""
086 - Spider in a cube.py

Created by Jason Sundram on 2010-09-09.
Copyright (c) 2010. All rights reserved.

Problem 86
07 January 2005

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. 
By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route is not always integer.

By considering all cuboid rooms with integer dimensions, up to a maximum size of M by M by M, 
there are exactly 2060 cuboids for which the shortest distance is integer when M=100, 
and this is the least value of M for which the number of solutions first exceeds two thousand; 
the number of solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first exceeds one million.
"""
from timed import timed
import psyco; psyco.full()

LIMIT = 1000 * 1000

@timed
def faster():
    """from tolstopuz, http://projecteuler.net/index.php?section=forum&id=86&page=3"""
    count = 0
    a = 1
    while True:
        for bc in xrange(1, 2 * a + 1):
                s = bc**2 + a**2
                root = s**.5
                if root == int(root):
                    count += min(bc, a + 1) - (bc + 1) // 2
        if LIMIT < count:
            break
        a += 1
    return a


def cuboids(M):
    print "cuboids(%d) . . ." % M
    count = 0
    for i in xrange(1, M+1):
        ii = i*i
        for j in xrange(i, M+1):
            ij = (i+j)**2
            for k in xrange(j, M+1):
                a, b = ij + k**2, (j+k)**2 + ii
                m = a if a < b else b # min(a, b) # min is really slow
                s = m**.5
                if s == int(s):
                    count += 1
        # if LIMIT < count: 
        #   print "exiting early"
        #   return count
    return count

def asearch(lo, hi, f, X):
    """ adapted from utils.bsearch
        the domain is [lo, hi). We find the closest integer x such that f(x) == X.
    """
    while lo < hi:
        mid = (lo + hi) // 2
        # print "%d, %d, %d" % (lo, mid, hi)
        midval = f(mid)
        if midval < X:
            lo = mid + 1
        elif midval > X: 
            hi = mid
        else:
            return mid
    return lo

@timed
def original_solution():
    """ original_solution took 3176086.529 ms
        The answer (original) is: 1818
    """
    # 100 ->    2060
    # 400 ->   40432
    # 1057 -> 318820
    # 2000 -> 1229543
    return asearch(1057, 2000, cuboids, 1000*1000)


def main():
    print 'The answer (original) is: %d' % faster   ()


if __name__ == '__main__':
    main()

