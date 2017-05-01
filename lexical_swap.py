# https://www.hackerrank.com/challenges/bigger-is-greater

from string import ascii_lowercase

n = int(raw_input())

for _ in xrange(n):
    word = raw_input()
    d_rep = [(ord(let)-97) for let in word]
    n_ = len(word)
    max_ = [None]*n_
    for i in xrange(n_-1, -1, -1):
        max_[i] = filter(lambda j: j[1] > d_rep[i], enumerate(d_rep[i+1:]))
        if len(max_[i])>0:
            break;
    while len(max_[i])==0 and i>=0:
        i-=1
    if i<0:
        print "no answer"
    else:
        j,v = min(max_[i], key=lambda x: x[1]*27+x[0])
        j+=i+1
        tmp = d_rep[i]
        d_rep[i]=v
        d_rep[j]=tmp
        d_rep = d_rep[:(i+1)]+sorted(d_rep[i+1:])
        #d_rep[k]=tmp
        print "".join(map(ascii_lowercase.__getitem__, d_rep))
    
