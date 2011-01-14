  #!/usr/bin/env python
# encoding: utf-8
"""
066 - Diophantine.py

Created by Jason Sundram on 2010-01-13.
Copyright (c) 2010. All rights reserved.

Problem 66
26 March 2004

Consider quadratic Diophantine equations of the form:

x**2 – D * y**2 = 1

For example, when D=13, the minimal solution in x is 649^(2) – 13×180^(2) = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3**2 – 2 * 2**2 = 1
2**2 – 3 * 1**2 = 1
9**2 – 5 * 4**2 = 1
5**2 – 6 * 2**2 = 1
8**2 – 7 * 3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

"""
from timed import timed
from utils import convergents, root_expansion, is_perfect_square
from itertools import count, ifilter, ifilterfalse


def wolfram_min(D):
    """The Glorious Pell Equation: http://mathworld.wolfram.com/PellEquation.html"""
    A = root_expansion(D)
    r = len(A) - 2
    
    # From math world, we know:
    # if r is odd, x = p(r), y = q(r) is a minimal solution
    # if r is even, x = p(2*r+1), y = p(2*r + 1)
    n = r if r & 1 else 2*r + 1
    
    x, y = convergents(A, n).pop()
    return D, x


@timed
def original_solution():
    """runtime on mbp is 362ms"""
    Dlist = ifilterfalse(is_perfect_square, xrange(1, 1001))
    solutions = map(wolfram_min, Dlist)
    (D, x) = max(solutions, key=lambda t : t[1])
    return D

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

