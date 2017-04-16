#!/bin/python
# https://www.hackerrank.com/contests/w31/challenges/accurate-sorting

import sys

def swap_sweep(ls):
    swapped=False
    for i in xrange(len(ls)-1):
        if ls[i]-ls[i+1]==1:
            ls[i],ls[i+1]=ls[i+1],ls[i]
            swapped=True
    return swapped

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    while swap_sweep(a):
        pass
    if a==sorted(a):
        print "Yes"
    else:
        print "No"
