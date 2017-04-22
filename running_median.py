# https://www.hackerrank.com/challenges/find-the-running-median
from bisect import bisect_left

class SortedList:
    def __init__(self):
        self.list = []
    def add(self, v):
        i=bisect_left(self.list, v)
        self.list.insert(i, v)
    def median(self):
        n_ = len(self.list)
        if n_%2==0:
            return (self.list[n_/2-1]+self.list[n_/2])/2.0
        return self.list[n_/2]

sl = SortedList()
n = int(raw_input())
for _ in xrange(n):
    v = float(raw_input())
    sl.add(v)
    print sl.median()
