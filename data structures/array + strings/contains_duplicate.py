
class Solution(object):
    #sets are unordered, unindexed, unique collection
    #used in membership testing, removing duplicates, math operations
    def containsDuplicate(self, nums):
        myset = set(nums)
        # print(myset)
        if len(myset) != len(nums):
            return True
        return False




s1 = Solution()
print(s1.containsDuplicate([3,5,4,6,3,4,5]))
        
        # #if there are any duplicate integers, they will be consecutive after sorting
        # nums.sort()
        # # if len(nums) == 1:
        # #     return False
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        
        
        #time limit exceeded
        
        # if len(nums) == 1:
        #     return False
        # for i in range(len(nums)):
        #     if nums[i] in nums[i+1:]:
        #         return True
        # return False
        