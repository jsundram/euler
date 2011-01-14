#!/usr/bin/env python
# encoding: utf-8
"""
054 - Poker Hands.py

Created by Jason Sundram on 2009-12-11.
Copyright (c) 2009. All rights reserved.

Problem 54
10 October 2003

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    * High Card: Highest value card.
    * One Pair: Two cards of the same value.
    * Two Pairs: Two different pairs.
    * Three of a Kind: Three cards of the same value.
    * Straight: All cards are consecutive values.
    * Flush: All cards of the same suit.
    * Full House: Three of a kind and a pair.
    * Four of a Kind: Four cards of the same value.
    * Straight Flush: All cards are consecutive values of same suit.
    * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand    Player 1            Player 2            Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
Pair of Fives               Pair of Eights
2       5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
Highest card Ace            Highest card Queen
3       2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds
4       4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven
5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    With Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

"""
from timed import timed
from collections import defaultdict
import traceback

value = lambda x: cards.index(x)    
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def score(hand):
    """ Rules:
    1) High Card: Highest value card. (13)
    2) One Pair: Two cards of the same value. (13)
    3) Two Pairs: Two different pairs. (13)
    4) Three of a Kind: Three cards of the same value. (13)
    5) Straight: All cards are consecutive values. (9)
    6) Flush: All cards of the same suit.
    7) Full House: Three of a kind and a pair. (13*12)
    8) Four of a Kind: Four cards of the same value. (13)
    9) Straight Flush: All cards are consecutive values of same suit. (9)
    10) Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. 1"""
    
    values, suits = zip(*[(s[:-1], s[-1]) for s in hand])
    
    high_card = max(values, key=value) 
    
    d = defaultdict(int)
    for v in values: d[v] += 1
    s = sorted(d.iteritems(), key = lambda (k,v):(v,k), reverse=True)
    s = [(k,v) for (k,v) in s if v > 1]
    get_high = lambda x: max([v for v in values if v not in x], key=value)
    if len(s) != 0:
        v, count = s[0]
        if count == 4:
            return (8, v, get_high(set(v)))
        elif count == 3:
            if len(s) == 1:
                return (4, v, get_high(set(v)))
            elif len(s) == 2: # full house
                return (7, v, s[1][0])
        elif count == 2:
            if len(s) == 2: # two pair
                return (3, s[1][0], v, get_high(set([v, s[1][0]])))
            else:
                return(2, v, get_high(set(v)))
    else:
        # Do we have a straight
        straight = True
        high = value(high_card)
        if 4 < high:
            for index in range(high-4, high+1):
                if cards[index] not in values:
                    straight = False;
                    break
        
        # flush
        flush = 1 == len(set(suits))
        low_card = min(values, key=value)
        
        if flush and straight:
            return (9, low_card)
        elif flush:
            return (6, high_card)
        elif straight:
            return (5, low_card)
            
    return (1, high_card)

def compare(score1, score2):
    i = cmp(score1[0], score2[0])
    place = 1
    while i == 0: 
        i = cmp(value(score1[place]), value(score2[place]))
        place += 1
    return i
        
def test():
    """
    1) High Card: Highest value card. (13)
    2) One Pair: Two cards of the same value. (13)
    3) Two Pairs: Two different pairs. (13)
    4) Three of a Kind: Three cards of the same value. (13)
    5) Straight: All cards are consecutive values. (9)
    6) Flush: All cards of the same suit.
    7) Full House: Three of a kind and a pair. (13*12)
    8) Four of a Kind: Four cards of the same value. (13)
    9) Straight Flush: All cards are consecutive values of same suit. (9)
    10) Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. 1
    """
    high = ['AS', 'KD', '3D', 'JD', '8H']
    assert(score(high) == (1, 'A'))
    pair = ['AS', 'AD', '2D', '3D', '4D']
    assert(score(pair) == (2, 'A')) 
    two_pair = ['AS', 'AD', 'KS', 'KD', '4D']
    assert(score(two_pair) == (3, 'A', 'K', '4')) 
    three = ['AS', 'AD', 'AH', 'KD', '4D']
    assert(score(three) == (4, 'A', 'K')) 
    straight = ['2S', '3D', '4H', '5D', '6D']
    assert(score(straight) == (5, '2')) 
    flush = ['2S', '3S', '4S', '5S', '7S']
    assert(score(flush) == (6, '7')) 
    full_house = ['2S', '2D', '3S', '3D', '3H']
    assert(score(full_house) == (7, '3', '2'))
    four =  ['KS', '3C', '3S', '3D', '3H']
    assert(score(four) == (8, '3', 'K'))
    straight_flush = ['2C', '3C', '4C', '5C', '6C']
    assert(score(straight_flush) == (9, '2'))
    royal_straight_flush = ['TC', 'JC', 'QC', 'KC', 'AC']
    assert(score(royal_straight_flush) == (9, '10'))
    
    
@timed
def original_solution():
    f = open('054 - Poker Hands.txt')
    count = 0
    for s in f.readlines():
        cards = s.strip().split(' ')
        p1 = cards[0:5]
        p2 = cards[5:10]
        try:
            if compare(score(p1), score(p2)) == 1:
                count += 1
        except Exception:
            print p1
            print p2
            print str(traceback.format_exc())
        
    f.close()
    return count


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

