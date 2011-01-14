# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

import math

N = 100
total = (N + 1) * N / 2
SquareOfSum = total ** 2
SumOfSquare = 0

# xrange treats the interval like this [start, end)
for i in xrange(1, N + 1):
    SumOfSquare += i**2

print SquareOfSum - SumOfSquare

# Runtime: O(n)
