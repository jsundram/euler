#!/usr/bin/env python
# encoding: utf-8
"""
083 - Minimal Path through Matrix.py

Created by Jason Sundram on 2010-09-09.
Copyright (c) 2010. All rights reserved.

Problem 83
19 November 2004

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, 
is indicated in bold red and is equal to 2297.

(See TEST matrix below)

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, 
from the top left to the bottom right by moving left, right, up, and down.
"""
from __future__ import with_statement
import os, sys
import networkx as nx

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
    """ original_solution took 254.301 ms
        The answer (original) is: 420740
    """
    matrix = get_data()
    # Construct Graph
    G = nx.DiGraph()
    rows, cols = len(matrix), len(matrix[0])
    for r in xrange(rows):
        for c in xrange(cols):
            if 0 < c:
                G.add_edge(r*cols + c, r*cols + c - 1, weight=matrix[r][c-1])
            if c < cols-1:
                G.add_edge(r*cols + c, r*cols + c + 1, weight=matrix[r][c+1])
            if 0 < r:
                G.add_edge(r*cols + c, (r-1)*cols + c, weight=matrix[r-1][c])
            if r < rows-1:
                G.add_edge(r*cols + c, (r+1)*cols + c, weight=matrix[r+1][c])
    # Calculate shortest path
    path = nx.shortest_path(G, 0, rows*cols-1, weighted=True)
    
    # Get cost for path
    s = 0
    for p in path:
        c = p % cols
        r = (p - c) / rows
        s += matrix[r][c]
    return s


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

