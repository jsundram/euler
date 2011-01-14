def isSquare(n):
    guess = n
    last = n + 1
    while( last > guess):
        print "n = ", n, "last = ", last, " guess = ", guess
        last = guess
        guess = (guess + n / guess) / 2
  
    return last*last == n

print isSquare(1)
print isSquare(244)
