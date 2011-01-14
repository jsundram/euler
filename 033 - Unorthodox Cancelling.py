#!/usr/bin/env python
# encoding: utf-8
"""
033 - Unorthodox Cancelling.py

Created by Jason Sundram on 2009-12-03.

Problem 33
20 December 2002

The fraction ^(49)/_(98) is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that
    ^(49)/_(98) = ^(4)/_(8), 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

import sys
import os

def gcd(a,b):
        """Euclid's algorithm for finding the greatest common divisor."""
        while a:
                a, b = b%a, a
        return b

def reduce_fraction(num, den):
    factor = gcd(num, den)
    return (num / factor, den / factor)
    
def cancel(num, den):
    """Cancels common digits from num and den, returns floats, and a string representation of the cancelled digit, or '' if none"""
    n = list(str(num))
    d = list(str(den))
    i = set(n).intersection(set(d))
    digit = ''
    if len(i):
        for digit in i:
            n.remove(str(digit))
            d.remove(str(digit))
        if len(n) != 0:
            num = float(''.join(n))
        if len(d) != 0:
            den = float(''.join(d))
    return (num, den, digit)
    
def main():
    fracs = []
    for den in xrange(11, 100):
        for num in xrange(11, den):
            frac = float(num) / float(den)
            (n, d, cancelled) = cancel(num, den)
            if d != 0 and cancelled != '0' and frac == (n / d):
                print "%d / %d == %d / %d (cancelled %s)" % (num, den, int(n), int(d), cancelled)
                fracs.append((int(n), int(d)))
                
    f_mult = lambda (n1, d1), (n2, d2) : (n1 * n2, d1 * d2)
    (top, bottom) = reduce(f_mult, fracs)
    print "product of all fracs = %d / %d." % reduce_fraction(top, bottom)

if __name__ == '__main__':
    main()

