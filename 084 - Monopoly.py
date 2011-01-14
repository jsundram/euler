#!/usr/bin/env python
# encoding: utf-8
"""
084 - Monopoly.py

Created by Jason Sundram on 2010-09-09.
Copyright (c) 2010. All rights reserved.

Problem 84
03 December 2004

In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	                                	C1
T2	                                	U1
H1	                                	C2
CH3	                                	C3
R4	                                	R2
G3	                                	D1
CC3	                                	CC2
G2	                                	D2
G1	                                	D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. 
Without any further rules we would expect to visit each square with equal probability: 2.5%. 
However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, 
they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. 
When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. 
There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; 
any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
    Advance to GO
    Go to JAIL
Chance (10/16 cards):
    Advance to GO
    Go to JAIL
    Go to C1
    Go to E3
    Go to H2
    Go to R1
    Go to next R (railway company)
    Go to next R
    Go to next U (utility company)
    Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. 
For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, 
the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, 
and it is the final square that the player finishes at on each roll that we are interested in. 

We shall make no distinction between "Just Visiting" and being sent to JAIL, 
and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these 
two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are 
JAIL (6.24%) = Square 10, 
E3 (3.18%) = Square 24, and 
GO (3.09%) = Square 00. 
So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string
"""
from timed import timed
import random

squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
num_squares = len(squares)
square_nums = dict(zip(squares, xrange(num_squares)))
counter = dict(zip(xrange(len(squares)), [0] * num_squares))
CC = [square_nums['GO'], square_nums['JAIL']] + [None] * 14
CH = [square_nums['GO'], square_nums['JAIL'], square_nums['C1'], square_nums['E3'], square_nums['H2'], square_nums['R1'], -3, 'NR', 'NR', 'NU'] + [None] * 6
NR = {square_nums['CH1'] : square_nums['R2'], square_nums['CH2'] : square_nums['R3'], square_nums['CH3'] : square_nums['R1']}
NU = {square_nums['CH1'] : square_nums['U1'], square_nums['CH2'] : square_nums['U2'], square_nums['CH3'] : square_nums['U1']}
random.shuffle(CC)
random.shuffle(CH)
position = 0
sides = 4

def roll():
    # i = random.randint(1, 6);return i, i
    return random.randint(1, sides), random.randint(1, sides)

def card(deck):
    # return random.choice(deck)
    card = deck.pop(0)
    deck.append(card)
    return card

def move():
    global position, CC, CH, NR, NU
    di1, di2 = roll()
    position = (position + di1 + di2) % num_squares
    if position == square_nums['G2J']:
        position = square_nums['JAIL']
    elif squares[position].startswith('CC'):
        # print "community chest: %s" % squares[position]
        c = card(CC)
        if c is not None:
            position = c
    elif squares[position].startswith('CH'):
        c = card(CH)
        # print "Chance: %s" % squares[position]
        if type(c) is int:
            if 0 <= c:
                position = c
            else:
                position += c
        elif type(c) is str:
            if c == 'NR': # go to the nearest railroad
                position = NR[position]
            elif c == 'NU':
                position = NU[position]
        # print "\tmoving to: %s" % squares[position]
    
    counter[position] += 1
    return di1 == di2
    
@timed
def original_solution():
    """ original_solution took 144.034 ms
        The answer (original) is: 101524
        runtime is a function of limit, below. with 4-sided di, converges fast. With 6-sided, I found over 500K turns to be necessary for stability.
    """
    limit = 10000
    
    for i in xrange(limit):
        doubles = move()
        
        double_count = 0
        while doubles:
            double_count += 1
            if double_count < 3:
                doubles = move()
            else:
                # print "3 doubles in a row! going to JAIL!"
                position = square_nums['JAIL'] # position = (position + di1 + di2) % num_squares
                counter[position] += 1
                doubles = False
    
    top = sorted(counter.iteritems(), key=lambda(k,v):(v,k), reverse=True)[:3]
    total = sum(counter.values())
    print 'top squares:', [(squares[i[0]], '%2.3f' % (100.0*i[1]/float(total))) for i in top]
    return ''.join('%02d' % i[0] for i in top)


def main():
    print 'The answer (original) is: %s' % original_solution()


if __name__ == '__main__':
    main()

