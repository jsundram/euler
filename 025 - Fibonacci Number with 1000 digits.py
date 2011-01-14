# The Fibonacci sequence is defined by the recurrence relation:
#
#    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#
# e.g. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the first term in the Fibonacci sequence to contain 1000 digits?

import math

# X is the Golden Ratio
ROOT_5 = math.sqrt(5)
X = (1.0 + ROOT_5) / 2.0

# Closed form for the Nth fibonacci number
def Fibonnaci(n):
    return math.floor(((X ** n) / ROOT_5) + .5)

NUM_DIGITS = 1000

# Want Fibonnaci(n) > 10^NUM_DIGITS - 1
# (N.B. 10^N is the smallest number with N+1 digits)
# So, solve:
# math.floor((X**N /ROOT_5) + .5) > 10**999
# get rid of the floor for now, we'll make up for it later.
# Log base 10 of both sides:
# math.log10(X**N / ROOT_5) > 999
# math.log10(X**N) - math.log10(ROOT_5) > 999
# N * math.log10(X) > 999 + math.log10(ROOT_5)
# N > (999 + math.log10(ROOT_5)) / math.log10(X)
N = math.ceil( (NUM_DIGITS - 1 + math.log10(ROOT_5)) / math.log10(X) )
print N
