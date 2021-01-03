'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.
'''

# In python, sorting is 0(n log n), usually.

from itertools import permutations

# 1) Brute force-ish
# complexity: intertools permutations - 0(nCr)
#             for loop - 0(N)              
def checkInclusion(s1,s2):
    perms = permutations(s1)
    permList = []
    # print(permList)
    for perm in list(perms):
        permList.append(''.join(perm))
    # print(permList)

    for eachperm in permList:
        if eachperm in s2:
            return True
    return False

# print(checkInclusion('ab','eidbaaaaaa'))



# 2)see s1 how many letters 
def checkInclusion_sorted(s1,s2):
    s1_sorted = ''.join(sorted(s1))
    len_s1 = len(s1)
    
    if s1_sorted in :
        return True
    return False

checkInclusion_sorted('cva','cascaa')


