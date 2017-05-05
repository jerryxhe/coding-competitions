#!/bin/python

# https://www.hackerrank.com/challenges/the-grid-search


import sys

def find_all(string, substring):
    index = []
    L = len(string)
    l = len(substring)
    # Needed for optimization
    for i in xrange(L-l+1):
        # Check if current grid row is equal to the first row of the pattern
        if string[i:i+l] == substring:
            index.append(i)
    return index

def find_pattern(grid, pattern):
    # Needed for optimization
    # R = rows, C = columns (grid is a list of strings)
    R, C = len(grid), len(grid[0])
    r, c = len(pattern), len(pattern[0])
    for i in xrange(R-r+1):
        indeces = find_all(grid[i], pattern[0])
        # Continue only if we found a match for the first row of 'pattern'
        if indeces:
            for idx in indeces:
                for j in xrange(i+1, i+r):
                    if pattern[j-i] != grid[j][idx:idx+c]:
                        break
                else:
                    # Loop finished normally
                    print 'YES'
                    return
    print "NO"
    return


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)
    find_pattern(G, P)
