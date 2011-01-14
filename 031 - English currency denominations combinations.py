#!/usr/bin/env python
# encoding: utf-8
"""
031 - English currency denominations combinations.py

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Created by Jason Sundram on 2009-11-23.
"""

import sys
import os


def ways_to_make(total, coins): 
    """Returns the number of ways to add coins with given denominations together to sum to total."""
    # solution from here: http://home.att.net/~numericana/answer/counting.htm
    coins.remove(1) # leave out pennies.
    total += 1 # deal with xrange upper limit.
    b = total * [1]
    a = total * [0]
    for c in coins:
        for i in xrange(0, total): 
            a[i] = b[i] 
            b[i] = 0
        for j in xrange(0, total, c):
            for k in xrange(0, total-j):
                b[j+k] += a[k]

    return b.pop()
    
def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    total = 200

if __name__ == '__main__':
	main()

