'''
qn -> You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements 
to the right of nums[i].

https://leetcode.com/problems/count-of-smaller-numbers-after-self/

concepts

bisect_left -> Locate the inserrtion point for X in a to maintain sorted order.

bisect.bisect_left(a, x, lo=0, hi=len(a)) -> lo and hi specify a subset of list
to be considered; by default entire list is used

sorted -> sort a list

pop -> list.pop(pos), default pos is -1
'''
import bisect 

def countSmaller(self,nums):
    sor = sorted(nums)
    res = [] 
    for el in nums:
        index = bisect.bisect_left(sor,el)
        res.append(index)
        sor.pop(index)
    return res
