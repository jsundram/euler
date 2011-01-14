# Starting in the top left corner of a 2x2 grid,
# there are 6 routes (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20x20 grid?

import time
def factorial(x):
    if (x < 2): return 1
    product = 1
    for i in xrange(2, x + 1):
        product *= i
    return product

start_time = time.time()

s = 20 # side dimension of the square grid.

# This is simple. We have to go over 's' times, and down 's' times.
# We can do it in whatever order we like. There are 2s! ways to order
# 2s "objects". However, because each down or over move is equivalent,
# we need to divide by the total number of arrangements of each of those.
# (s! for each)
answer = factorial(2 * s) / (factorial(s) ** 2)
total_time = time.time() - start_time

print answer
print "Elapsed: ", total_time, "seconds"
