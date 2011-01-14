#!/usr/bin/env python
# encoding: utf-8
"""
093 - Sequence Generators.py

Created by Jason Sundram on 2010-09-22.
Copyright (c) 2010. All rights reserved.

Problem 93
15 April 2005

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, -, *, /) 
and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8  = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, 
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 
1 to n, can be obtained, giving your answer as a string: abcd.
"""
from __future__ import division # important. otherwise we get shitty division, like 5/4 = 1
import time
from timed import timed
from utils import permutations, combinations, product

def is_int(n):
    return n > 0 and int(n) == n

def largest_continuous_range_new(s):
    """ More optimized for this problem, courtesy of JitteryWombat. 
        Doesn't make a noticeable impact on runtime, but short and sweet."""
    for i in xrange(1, len(s)):
        if i not in s:
            return i-1

def largest_continuous_range(l):
    m, c = 0, 0
    for a, b in zip(l, l[1:]):
        if b - a == 1: 
            c += 1
        else:
            m = max(m, c)
            c = 0
    return max(m, c) + 1

@timed
def original_solution():
    """ original_solution took 584.394 ms
              584.394 ms (write is_int inline instead of as a function call)
              741.234 ms (build a table of funcs instead of eval inline)
            13419.094 ms (intuition: solution won't have a 0 in it (useless!))
            20296.724 ms (intuition: solution needs to have 1 in it)
            50730.742 ms (save list of all operator combos instead of dynamic generation)
            51467.405 ms (format instead of 3 string replaces)
            53080.543 ms (essential set of combos)
            91008.076 ms (initial)
        The answer (original) is: 1258
    """
    # all possible combinations of operators
    olist = [p for p in product(['+', '-', '*', '/'], repeat=3)] 
    # all possible parenthesizations
    combos = ['(a %c (b %c c)) %c d', '((a %c b) %c c) %c d', 'a %c (b %c (c %c d))', 'a %c ((b %c c) %c d)', '(a %c b) %c (c %c d)']
    # all possible functions
    funcs = [eval('lambda a,b,c,d : %s' % (c % o)) for c in combos for o in olist]  
    
    m, answer = 0, ''
    for numbers in combinations(xrange(1, 10), 4):
        if not 1 in numbers: continue # intuition about requirements for solution
        outcomes = set()
        for a,b,c,d in permutations(numbers):
            for f in funcs:
                try:
                    n = f(a,b,c,d)
                    if 0 < n and int(n) == n:
                        outcomes.add(n)
                except ZeroDivisionError:
                    pass
        lcr = largest_continuous_range(sorted(outcomes)) #lcr = largest_continuous_range_new(outcomes)
        if m < lcr:
            m, answer = lcr, ''.join(map(str, numbers))
            print 'new max: %d from %s' % (m, answer)
    return answer


def main():
    print 'The answer (original) is: %s' % original_solution()


if __name__ == '__main__':
    main()

