# sample input
#
# Input: 
# 5
# 2 100 200
# 3 110 190
# 4 105 145
# 1 90 150
# 5 102 198
# 
# Output:
# 3 0
# 4 0
# 1 1
# 5 2
# 2 3


from collections import defaultdict

min_start_time = 10**18
max_finish_time = 0
n = int(raw_input())
st_size = []
import heapq
from bisect import bisect_left,bisect_right

class Node:
    def __init__(self, spaceshipID, start_time, fin_time):
        self.start_time = start_time
        self.fin_time = fin_time
        self.spaceshipID = spaceshipID
        self.data = []
        self.next_ = None
        
    def add_another(self, fin_time, spaceshipID, start_time):
        if fin_time < self.fin_time:
            heapq.heappush(self.data, (fin_time, spaceshipID, start_time))
        elif start_time==self.start_time:
            return
        else:
            if self.next_ is not None:
                self.next_.add_another(fin_time, spaceshipID, start_time)
            else:
                self.next_ = Node(spaceshipID, start_time,fin_time)
                
    def lt(self, fin_time_ref): # a destructive operation, only should be performed after this node is no longer needed
        tup = [0] 
        while len(self.data)>0 and tup[0] < fin_time_ref:
            tup = heapq.heappop(self.data)
            yield (tup[1],tup[2], tup[0])
            

import operator
spaceships = []
for _ in xrange(n):
    spaceships.append(map(int, raw_input().split(" "))) #     [spaceshipID, start_time, fin_time] 
    
def start_time_compare(x, y):
    return x[1] - y[1]
    
spaceships.sort(cmp=start_time_compare)  
n_spaceships = len(spaceships)
avg_duration = sum([(fin_t - st_t) for [_, st_t, fin_t] in spaceships])/float(n_spaceships)

earliest_time = spaceships[0][1]
nbuckets = int((spaceships[-1][2] - earliest_time)/avg_duration)+1

st_times = [row[1] for row in spaceships]
buckets = [None]*nbuckets
st_dividers = [None]*nbuckets

for i in xrange(nbuckets):
    j = bisect_left(st_times, earliest_time+avg_duration*i)
    j = min(j, n_spaceships-1)
    tup = spaceships[j]
    if st_dividers[i-1] is not None and st_dividers[i-1] == tup[1]:
        continue
    buckets[i] = Node(*tup)
    st_dividers[i] = tup[1]

for [spaceshipID, start_time, fin_time] in spaceships:
    i = bisect_right(st_dividers, start_time)
    if st_dividers[i-1]==start_time:
        continue
    buckets[i].add_another(fin_time, spaceshipID, start_time)    

scores = []
for i in xrange(nbuckets-1, -1, -1):
    bucket = buckets[i]
    if i<nbuckets-1:
        extras = [it for it in buckets[i+1].lt(bucket.fin_time)]
    else:
        extras = []
    scores.append([bucket.spaceshipID, len(bucket.data)+len(extras)])
    while bucket.next_ is not None:
        bucket = bucket.next_
        extras = filter(lambda tup: tup[2]< bucket.fin_time, extras)
        scores.append([bucket.spaceshipID, len(bucket.data)])

print st_dividers

for id_,score_ in sorted(scores, key=operator.itemgetter(1), reverse=True):
    print id_, score_
