# Pythagorean triplet is a < b < c | a**2 + b**2 = c**2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

# N.B. For positive integers m,n | m < n.
#   n**2 - m**2, 2mn, and n**2 + m**2 form a Pythagorean triple.
#
# used Simms to enumerate triples:
# http://www.math.clemson.edu/~simms/neat/math/pyth/npyth.html
for n in xrange(1,200):
    t = math.floor( (3 + math.sqrt(8 * n - 7)) / 2 )
    s = n -(t**2 - 3*t + 2) / 2
    x = 2*s*t
    y = t**2 -s**2
    z = t**2 +s**2
    if ((x + y + z) == 1000):
        print x, y, z, " = ", x*y*z,"\n"
