# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

import math
from timed import timed

@timed
def original_solution(N):
    """runtime on mba is 0.026ms"""
    total = (N + 1) * N / 2
    SquareOfSum = total ** 2
    SumOfSquare = 0

    # xrange treats the interval like this [start, end)
    for i in xrange(1, N + 1):
        SumOfSquare += i**2

    return SquareOfSum - SumOfSquare

def main():
    print 'The answer (original) is: %d' % original_solution(100)

if __name__ == '__main__':
    main()

# Runtime: O(n)
