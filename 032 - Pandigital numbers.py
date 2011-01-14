#!/usr/bin/env python
# encoding: utf-8
"""
032 - Pandigital numbers.py

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Created by Jason Sundram on 2009-11-23.
"""

import sys
import os

upper_limit = 10000
pandigits = set('123456789')
def inner_loop(i):
    products = set()
    for j in xrange(0, upper_limit):
        k = i*j
        s = str(i) + str(j) + str(k)
        n = len(s)
        if 9 < n: break
        
        if set(s) == pandigits:
            print "%d x %d = %d" % (i, j, k) # output won't be unique since we're in inner loop
            products.add(k)
    return products

def main():
    """Brute Force. Compute all products, and check if the string A x B = C contains all of 123456789. """
    products = set()
    for i in xrange(0, upper_limit):
        products.update(inner_loop(i))
    m = sum(products)
    print m
    return m

if __name__ == '__main__':
    main()

