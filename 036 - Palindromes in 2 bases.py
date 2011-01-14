#!/usr/bin/env python
# encoding: utf-8
"""
036 - Palindromes in 2 bases.py

Created by Jason Sundram on 2009-12-03.

The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

import sys
import os
from timed import timed # helper for timing.

def bin(n):    
    octmap = {'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}
    return ''.join([octmap[d] for d in oct(n)]).lstrip("0")
    
def isPalindrome(s):
    return s[::-1] == s # WTF python, why you so cool?



@timed 
def functional_solution():
    """Don't need to look at even numbers (end with 0 base 2)"""
    return sum([i for i in xrange(1, 1000000, 2) if isPalindrome(str(i)) and isPalindrome(bin(i))])
    
@timed    
def original_solution():
    palindromes = []
    for i in xrange(0, 1000000):
        if isPalindrome(str(i)) and isPalindrome(bin(i)):
            #print i
            palindromes.append(i)
    
    return sum(palindromes)

def main():
    print 'The answer (original) is: %d' % original_solution()
    print 'The answer (functional) is: %d' % functional_solution()
    
if __name__ == '__main__':
    main()

