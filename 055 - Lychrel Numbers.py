#!/usr/bin/env python
# encoding: utf-8
"""
055 - Lychrel Numbers.py

Created by Jason Sundram on 2009-12-15.
Copyright (c) 2009. All rights reserved.

Problem 55
24 October 2003

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
A number that never forms a palindrome through the reverse and add process is called a Lychrel number. 
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. 

In addition you are given that for every number below ten-thousand, it will either:
 (i) become a palindrome in less than fifty iterations, or, 
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. 

In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 
    4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

"""
from timed import timed

def is_palindrome(n):
    s = str(n)
    N = len(s)
    for i in range(N/2):
        if s[i] != s[N-i-1]:
            return False
    return True

def rev(n):
    return int(''.join(reversed(str(n))))
    
def is_lychrel(N, limit=50):
    i = 1
    n = N
    while i <= limit:
        s = n + rev(n)
        # print "%d + %d = %d" % (n, rev(n), s)
        if is_palindrome(s):
            #print ("%d is a palindrome after %d iterations: %s" % (N, i, str(s)))
            return False
        n = s
        i += 1
    #print "%d is lychrel after %d iterations"% (N, i)
    return True
        
@timed
def original_solution():
    return len(filter(is_lychrel, xrange(10*1000)))


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

