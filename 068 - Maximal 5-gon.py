#!/usr/bin/env python
# encoding: utf-8
"""
068 - Maximal 5-gon.py

Created by Jason Sundram on 2010-03-03.
Copyright (c) 2010. All rights reserved.

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

   4
    \
     3
    /  \
   1  - 2 - 6
  /
5

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), 
each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total   Solution Set
9       4,2,3; 5,3,1; 6,1,2
9       4,3,2; 6,2,1; 5,1,3
10      2,3,5; 4,5,1; 6,1,3
10      2,5,3; 6,3,1; 4,1,5
11      1,4,6; 3,6,2; 5,2,4
11      1,6,4; 5,4,2; 3,2,6
12      1,5,6; 2,6,4; 3,4,5
12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; 
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
What is the maximum 16-digit string for a "magic" 5-gon ring?

        X
         \
          X   X
         / \ /
        X   X
       /|   |
      X X---X--X
        |
        X
"""
from timed import timed
from utils import permutations

def structure(l):
    """Take a list of numbers ordered by perimeter, interior, and turn them into a set of 3-tuples respresenting the 5-gon ring"""
    a,b,c,d,e,f,g,h,i,j = l
    return [a,f,g, b,g,h, c,h,i, d,i,j, e,j,f]
    
def is_magic(l):
    """Is the 5-gon described by l a magic 5-gon?"""
    r = structure(l)
    return sum(r[:3]) == sum(r[3:6]) == sum(r[6:9]) == sum(r[9:12]) == sum(r[12:15])

@timed
def original_solution():
    """runtime on mbp is 51ms"""
    # generate all possible 16 digit strings that have 6-10 as external nodes, and start with 6
    # so, that's 6 + {all permutations of 7-10} on the outside, and all permutations of 1-5 on the inside
    # filter down to the ones that are magic, choose the max.
    best = 0
    for outside in permutations([7,8,9,10]):
        for inside in permutations([1,2,3,4,5]):
            l = (6,) + outside + inside
            if is_magic(l):
                i = int(''.join(map(str, structure(l))))
                print "magic: %d" % i
                if best < i: 
                    best = i
                
    return best

    
def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

