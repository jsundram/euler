# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

import time
start_time = time.time()

 
answer = sum(int(ch) for ch in str(2**1000))
    

time_elapsed = time.time() - start_time

print answer
print "Time elapsed: ", time_elapsed, " second(s)"

    
    
