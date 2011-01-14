#!/usr/bin/env python
# encoding: utf-8
"""
079 - Guess Password.py

Created by Jason Sundram on 2010-08-25.
Copyright (c) 2010. All rights reserved.

Problem 79
17 September 2004

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
from __future__ import with_statement
import os, sys
from timed import timed

def get_data(fix=str.strip):
    this = os.path.join(sys.path[0], sys.argv[0])
    datafile = this.replace('.py', '.txt')
    with open(datafile) as f:
        return map(fix, f.readlines())

@timed
def original_solution():
    """ original_solution took 0.346 ms
        The answer (original) is: 73162890
    """
    # 0) Read the data.
    data = list(set(get_data())) # redundancy doesn't help.
    
    # 1) Make a list of all the characters we have
    c = []
    for i in map(list, zip(*data)):
        c.extend(i)
    chars = list(set(c))
    
    # 2) Define a compare function over those characters using the data.
    def data_compare(c1, c2):
        for d in data:
            if c1 in d and c2 in d:
                return cmp(d.index(c1), d.index(c2))
    
    # 3) Perform sort using the custom compare.
    password = ''.join(sorted(chars, cmp=data_compare))
    
    # 4) test to make sure the password meets all of the clues we were given.
    for d in data:
        indices = map(password.index, d)
        assert(indices == sorted(indices))
    
    return int(password)


def main():
    print 'The answer (original) is: %d' % original_solution()
    topological_sort()


if __name__ == '__main__':
    main()

