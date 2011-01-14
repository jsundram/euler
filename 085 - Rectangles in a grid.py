#!/usr/bin/env python
# encoding: utf-8
"""
085 - Rectangles in a grid.py

Created by Jason Sundram on 2010-09-09.
Copyright (c) 2010. All rights reserved.

By counting carefully it can be seen that a rectangular grid measuring 3 (horiz) by 2 (vertical) contains eighteen rectangles:
1x1: 6
2x1: 4
3x1: 2
1x2: 3
2x2: 2
3x2: 1

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""
from timed import timed
import psyco; psyco.full()

def count(m, n):
     return m * (m+1) * n * (n+1) / 4

@timed
def original_solution():
    """ original_solution took 1.154 ms
        The answer (original) is: 2772
    """
    target = 2000 * 1000
    radius = 100
    mindist = target
    dims = 0, 0
    assert(count(3,2) == 18)
    for m in xrange(1, 500):
        for n in xrange(m, 500):
            c = count(m, n)
            if c > target + radius: break # pretty sure we can get closer than 100
            dist = abs(target - c)
            if dist < mindist:
                mindist = dist
                dims = m,n
    print dims, count(*dims), abs(target - count(*dims))
    return dims[0] * dims[1]

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

