#!/usr/bin/env python
# encoding: utf-8
"""
094 - Almost Equilateral.py

Created by Jason Sundram on 2010-09-23.
Copyright (c) 2010. All rights reserved.

Problem 94
29 April 2005

It is easily proved that no equilateral triangle exists with integral length sides and integral area. 
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""
from timed import timed
from utils import is_perfect_square

def integral_area(a, b, c):
    # use heron's formula
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))
    return is_perfect_square(area)

def p(x):
    r = 0
    if integral_area(x, x, x + 1):
        #print x, x, x+1
        r += 3*x + 1
    if integral_area(x, x, x - 1):
        #print x, x, x-1
        r += 3*x - 1
    return r

@timed 
def faster():
    """http://mathworld.wolfram.com/HeronianTriangle.html -> http://cis.csuohio.edu/~somos/lp04.c"""
    
@timed
def original_solution():
    N = 10**9
    limit = int(N / 3) + 1 
    total = 5 # 1,1,2 (not included below)
    for side in xrange(2, limit):
        total += p(side)
        if side % 10**6 == 0: print side
    return total


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

