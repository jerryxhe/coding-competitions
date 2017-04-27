# https://www.hackerrank.com/challenges/stepping-stones-game

from math import sqrt
T = int(raw_input())

for _ in xrange(T):
    n = int(raw_input())
    k=int(sqrt(2*n))
    if k*(k+1) != 2*n:
        print "Better Luck Next Time"
    else:
        print "Go On Bob "+str(k)
