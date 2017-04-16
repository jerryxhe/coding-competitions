#!/bin/python
# this code is not working

# https://www.hackerrank.com/contests/w31/challenges/zero-one-game

import sys


g = int(raw_input().strip())

for a0 in xrange(g):
    n = int(raw_input().strip())
    sequence = map(int, raw_input().strip().split(' '))
    offset = (sequence[0] | sequence[-1] +1)%2
    n_removables = 0
    len_ = len(sequence)
    for i in xrange(1, len_-1):
        if sequence[i-1]==0 and sequence[i+1]==0:
            n_removables += 1
        elif i>2 and i < len_-2 and sequence[i]==0 and sequence[i-1]*sequence[i-2]==0 and sequence[i+1]*sequence[i+2]==0:
            n_removables += 1
    if (n_removables+offset) % 2 == 0:
        print 'Alice'
    else:
        print 'Bob'
