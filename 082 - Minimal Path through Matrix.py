#!/usr/bin/env python
# encoding: utf-8
"""
082 - Minimal Path through Matrix.py

Created by Jason Sundram on 2010-09-08.
Copyright (c) 2010. All rights reserved.

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, 
and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

(See matrix called TEST below)

Find the minimal path sum, in matrix.txt a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
"""
from __future__ import with_statement
import os, sys
# import psyco; psyco.full()
from timed import timed

TEST = [[131, 673, 234, 103,  18],
        [201,  96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524,  37, 331]]


def get_data(test=False):
    if test: return TEST
    datafile = os.path.join(sys.path[0], sys.argv[0]).replace('.py', '.txt')
    with open(datafile) as f:
        return [map(int, line.strip().split(',')) for line in f]

@timed
def original_solution():
    """ original_solution took 13.089 ms
        The answer (original) is: 260324
        
        borrowed from recursive: http://projecteuler.net/index.php?section=forum&id=82&page=2
        (i had used networkx, which was slow ~ 10 minutes)
    """
    m = get_data()
    opt = [[row[0]] for row in m]
    rows, cols = len(m), len(m[0])
    for col in xrange(1, cols):
        # right
        for row in xrange(rows):
            opt[row].append(m[row][col] + opt[row][col - 1])
        
        # up
        for row in xrange(1, rows):
            if opt[row - 1][col] + m[row][col] < opt[row][col]:
                opt[row][col] = opt[row - 1][col] + m[row][col]
        
        # down
        for row in reversed(xrange(rows - 1)):
            if opt[row + 1][col] + m[row][col] < opt[row][col]:
                opt[row][col] = opt[row + 1][col] + m[row][col]
        
    return min(row[-1] for row in opt)



def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

