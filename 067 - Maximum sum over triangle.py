#!/usr/bin/env python
# encoding: utf-8
"""
067 - Maximum sum over triangle.py

Created by Jason Sundram on 2010-02-26.
Copyright (c) 2010. All rights reserved.

Problem 67
09 April 2004

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! 
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)

"""
from __future__ import with_statement
from timed import timed
import os, sys

def get_triangle(data):
    with open(data) as f:
        return [map(int, line.split()) for line in f]

def tuples(l, n=2):
    """ returns n-tuples from l.
        e.g. tuples(range(4), n=2) -> [(0, 1), (1, 2), (2, 3)]
    """
    return zip(*[l[i:] for i in range(n)])

def pythonic_max(A):
    while len(A) > 1:
        prev = [max(i,j) for (i,j) in tuples(A.pop())]
        A[-1] = map(sum, zip(A[-1], prev)) # want +=, will settle for this	
    return A[0][0]
    
def get_max_sum(A):
    # Use algorithm from 18, rewritten a bit
    # Rewrite A from the bottom up, so that the maximum sum is
    # flowed back up towards the top.
    A.reverse()
    for row in xrange(1,len(A)):
        # For each row entry, add the greater of the two entries beneath it.
        for j in xrange(0, len(A[row])):
            A[row][j] += max(A[row - 1][j], A[row - 1][j+1])
    return A[-1][-1]

@timed
def original_solution():
    "runtime on mbp is 7ms"
    this = os.path.join(sys.path[0], sys.argv[0])
    triangle_file = this.replace('.py', '.txt')
    
    A = get_triangle(triangle_file)

    return pythonic_max(A)


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

