#!/usr/bin/env python
# encoding: utf-8
"""
034 - Factorions.py

Created by Jason Sundram on 2009-12-03.

Problem 34
03 January 2003

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import sys
import os

# These numbers are called Factorions: http://mathworld.wolfram.com/Factorion.html

# Used graphing calculator: http://www.wolframalpha.com/input/?i=9!*x+%3D+10^x
# to find where factorial(9) * x == 10**x. Turns out x ~ 6.36346
upper_bound = int(10.0**6.37)

from operator import mul
def factorial(n):
    return reduce(mul, xrange(1, n+1), 1)

def digits(n):
    return map(int, list(str(n)))

def functional_solution():
    return sum([i for i in xrange(3, upper_bound) if sum(map(factorial, digits(i))) == i])

def original_solution():
    curious = []
    for i in xrange(3, upper_bound):
        if sum(map(factorial, digits(i))) == i:
            print i
            curious.append(i)
    return sum(curious)

def main():
    return functional_solution()


if __name__ == '__main__':
    main()

