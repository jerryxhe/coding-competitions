# https://www.hackerrank.com/challenges/manasa-loves-maths
from itertools import permutations
n = int(raw_input())

def gdigits(int_):
    while int_!=0:
        yield int_%10
        int_ /=10

for _ in xrange(n):
    num_ = raw_input()
    yes_printed = False
    for str_num in permutations(num_, min(3, len(num_))):
        if int(str_num[-1])%2==1:
            continue
        if int("".join(str_num)) % 8==0:
            print "YES"
            yes_printed = True
            break
    if not yes_printed:
        print "NO"
