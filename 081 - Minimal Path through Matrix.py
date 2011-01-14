#!/usr/bin/env python
# encoding: utf-8
"""
081 - Minimal Path through Matrix.py

Created by Jason Sundram on 2010-08-25.
Copyright (c) 2010. All rights reserved.

Problem 81
22 October 2004

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

DRRDRDDR (down, right, etc)
Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""
from __future__ import with_statement
import os, sys
import networkx as nx
from timed import timed

def get_data():
    this = os.path.join(sys.path[0], sys.argv[0])
    datafile = this.replace('.py', '.txt')
    matrix = []
    with open(datafile) as f:
        for line in f:
            matrix.append(map(int, line.strip().split(',')))
    return matrix

@timed
def original_solution():
    matrix = get_data()
    # matrix = [ # use the test data
    #             [131, 673, 234, 103, 18],
    #             [201, 96, 342, 965, 150],
    #             [630, 803, 746, 422, 111],
    #             [537, 699, 497, 121, 956],
    #             [805, 732, 524, 37, 331]
    #         ]
    
    # let's have some fun with networkx.
    G = nx.DiGraph()
    rows, cols = len(matrix), len(matrix[0])
    for r in xrange(rows):
        for c in xrange(cols):
            if c < cols-1:
                G.add_edge(r*cols + c, r*cols + c + 1, weight=matrix[r][c+1])
            if r < rows-1:
                G.add_edge(r*cols + c, (r+1)*cols + c, weight=matrix[r+1][c])
                
    path = nx.shortest_path(G, 0, rows*cols-1, weighted=True)
    
    # convert the path into the sum...
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

