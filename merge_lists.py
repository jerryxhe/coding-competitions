# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists

import sys
sys.setrecursionlimit(1000)

def MergeLists(headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA
    merged =  Node()
    if headA.data < headB.data:
        merged.data = headA.data
        merged.next = MergeLists(headA.next, headB)
        return merged
    else:
        return MergeLists(headB, headA)
