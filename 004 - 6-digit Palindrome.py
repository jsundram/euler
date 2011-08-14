# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is:
#   9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math
from timed import timed

def palindrome(s):
    """purpose-built for this problem"""
    if len(s) == 6:
        return s[0] == s[5] and s[1] == s[4] and s[2] == s[3]
    
@timed
def original_solution():
    """runtime on mba is 59ms"""
    best = 0;
    for i in xrange(999, 100, -1):
         for j in xrange(999, i, -1):
              product = i * j
              if best < product and palindrome(str(product)):
                  best = product
    return best

def main():
    print "Original solution is: ", original_solution()

if __name__ == '__main__':
    main()

#runtime: O(N)
