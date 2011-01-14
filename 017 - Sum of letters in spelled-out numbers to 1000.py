# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
#   e.g. 342 (three hundred and forty-two) contains 23 letters
#   e.g. 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


import time
start_time = time.time()

# First, let us count some letters:
# one two three four five six seven eight nine
# 3   3   5     4    4    3   5     5     4    = 36  
# ten eleven twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
# 3   6      6       8         8         7        7        9          8         8 = 70
# twenty thirty forty fifty sixty seventy eighty ninety
# 6      6      5      5     5     7       6      6 =  46
# hundred => 7
# thousand => 8

# Part I: 1-99
# PartI = 36      + # (one-nine)#
#         70      + # (ten-nineteen)
#         8 * 36  + # (one-nine for 20-90)
#         10 * 46   # (twenty - ninety)
PartI = 36 + 70 + 8*36 + 10*46

# Part II 
# For everything over one hundred, we have base (1-9) + hundred + and + number
# Note that for 100, 200, there is no "and".

# PartII =    100 * 36    +   # each base gets used 100 times 
#             9 * 99 * 10 +   # hundred and
#             9 * 7       +   # hundred (no "and")
#             10 * PartI  +   # 1-99 for each of 10 groups of 100.
#             11              # one thousand
PartII = 100 * 36 + 9 * 99 * 10 + 9 * 7 + 10 * PartI + 11

print PartII
time_elapsed = time.time() - start_time

print "Time elapsed: ", time_elapsed, " second(s)"
    
    
