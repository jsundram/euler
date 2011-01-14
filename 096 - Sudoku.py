#!/usr/bin/env python
# encoding: utf-8
"""
096 - Sudoku.py

Created by Jason Sundram on 2010-09-20.
Copyright (c) 2010. All rights reserved.

Problem 96
27 May 2005

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles,
however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
and 3 by 3 box contains each of the digits 1 to 9. 

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although
it may be necessary to employ "guess and test" methods in order to eliminate options (there
is much contested opinion over this). The complexity of the search determines the difficulty
of the puzzle; the example above is considered easy because it can be solved by straight
forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty
different Su Doku puzzles ranging in difficulty, but all with unique solutions.

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner
of each solution grid; for example, 483 is the 3-digit number found in the top left corner of
the solution grid above.
"""
from timed import timed
## Solve Every Sudoku Puzzle

## See http://norvig.com/sudoku.html

## Throughout this program we have:
##   r is a row,    e.g. 'A'
##   c is a column, e.g. '3'
##   s is a square, e.g. 'A3'
##   d is a digit,  e.g. '9'
##   u is a unit,   e.g. ['A1','B1','C1','D1','E1','F1','G1','H1','I1']
##   grid is a grid,e.g. 81 non-blank chars, e.g. starting with '.18...7...
##   values is a dict of possible values, e.g. {'A1':'12349', 'A2':'8', ...}

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[])) - set([s])) for s in squares)

################ Parse a Grid ################

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def get_grids():
    lines = file(__file__.replace('.py', '.txt')).read().strip().split('\r\n')
    grids = []
    for l in lines:
        if l.startswith('G'):
            grids.append('=')
        else:
            grids.append(l)
    gstring = ''.join(grids)
    grids = gstring.split('=') # haha
    return grids[1:]

################ Constraint Propagation ################

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    
    return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d, '')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

################ Search ################

def solve(grid):
    return search(parse_grid(grid))

def first(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return first(search(assign(values.copy(), s, d)) for d in values[s])

def display(values):
    "Display these values as a 2-D grid."
    width = 1 + max(len(values[s]) for s in squares)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols)
        if r in 'CF': print line
    print

@timed
def original_solution():
    """ original_solution took 583.215 ms
        The answer (original) is: 24702
    """
    grids = get_grids()
    s = 0
    for i, grid in enumerate(grids):
        values = solve(grid)
        s += int(values['A1'] + values['A2'] + values['A3'])
        # display(grid_values(values))
    return s


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

