#!/usr/bin/env python
# encoding: utf-8
"""
028 - Spiral Sums.py

Created by Jason Sundram on 2009-11-07.

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25 
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Write some out by hand:
73 74 75 76 77 78 79 80 81
72 43 44 45 46 47 48 49 50
71 42 21 22 23 24 25 26 51
70 41 20  7  8  9 10 27 52
69 40 19  6  1  2 11 28 53
68 39 18  5  4  3 12 29 54
67 38 17 16 15 14 13 30 55
66 37 36 35 34 33 32 31 56
65 64 63 62 61 60 59 58 57
"""

import sys
import os
import operator
def sum_diagonals(n):
    """Returns the sum of the diagonals of an n by n spiral formed as described.
       Uses a bit of mathematical insight (i.e. not brute force)
    """
    center = [1]
    upper_right = [    i**2     for i in range(3, n+1, 2)]
    upper_left  = [1 + i**2 - i for i in range(3, n+1, 2)]
    
    lower_left  = [1 + i**2     for i in range(2, n, 2)]
    lower_right = [1 + i**2 - i for i in range(2, n, 2)]
    
    # This is equivalent to: 
    # return sum(upper_right) + sum(upper_left) + sum(lower_left) + sum(lower_right) + sum(center)
    return reduce(operator.add, map(sum, [upper_right, upper_left, lower_left, lower_right, center]))

# Use one polynomial to sum the corners for a given square.
corners = lambda x : 4*x**2 - 6*x + 6

def sum_diagonals_fancy(n):
    """Final answer"""
    return 1 + reduce(operator.add, map(corners, xrange(3, n+1, 2)))

def sum_diagonals_recursive(n):
    """Saw in forums, uses tail recursion. Tidied up a bit"""
    if n == 1: return 1
    return corners(n) + sum_diagonals_recursive(n-2)


def main():
    print sum_diagonals(1001)


if __name__ == '__main__':
	main()

