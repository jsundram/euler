#!/usr/bin/env python
# encoding: utf-8
"""
089 - Roman Numerals.py

Created by Jason Sundram on 2010-09-12.
Copyright (c) 2010. All rights reserved.

Problem 89
18 February 2005

The rules for writing Roman numerals allow for many ways of writing each number (see FAQ: Roman Numerals). 
However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers 
written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending 
units and obey the subtractive pair rule (see FAQ for the definitive rules for this problem).
FAQ: http://projecteuler.net/index.php?section=faq&ref=roman_numerals

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""
from __future__ import with_statement
import sys, os
from timed import timed

numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
nv = dict(zip(numerals, values))

def get_data():
    datafile = os.path.join(sys.path[0], sys.argv[0]).replace('.py', '.txt')
    with open(datafile) as f:
        return [line.strip() for line in f]

def to_roman(n):
    """int -> str"""
    # use a table: http://en.wikipedia.org/wiki/Roman_numerals
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] # 0-9 
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 10-90
    huns = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] # 100-900
    mils = ['', 'M', 'MM', 'MMM', 'MMMM']
    
    s = ''
    for place, table in zip([1000, 100, 10, 1], [mils, huns, tens, ones]):
        q = n // place
        s += table[q]
        #print "%d: %ds place, trying to write %d (table %s)" % (n, place, q, table)
        n -= q*place
    return s


def from_roman(s):
    """str -> int"""
    n = 0
    for c in s:
        n += nv[c]
    
    # Subtraction:
    # Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
    # I can only be placed before V and X.
    # X can only be placed before L and C.
    # C can only be placed before D and M.
    if 'IV' in s or 'IX' in s:
        n -= 2
    if 'XL' in s or 'XC' in s:
        n -= 20
    if 'CD' in s or 'CM' in s:
        n -= 200
    return n

@timed
def original_solution():
    """ original_solution took 6.500 ms
        The answer (original) is: 743
    """
    romans = get_data()
    original_length = sum([len(s) for s in romans])
    rewritten = [to_roman(from_roman(s)) for s in romans]
    new_length = sum([len(s) for s in rewritten])
    return original_length - new_length


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

