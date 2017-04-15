#!/bin/python

# https://www.hackerrank.com/challenges/utopian-tree

import sys

height_cache = [1]
def heightAt(t):
    if t < len(height_cache):
        return height_cache[t]
    elif t > len(height_cache):
        for t_ in range(len(height_cache), t+1):
            height_cache.append(heightAt(t_))
        return height_cache[t]
    else:
        if t%2==1:
            return height_cache[t-1]*2
        else:
            return height_cache[t-1]+1
    

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print heightAt(n)
