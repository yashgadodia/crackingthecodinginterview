# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # #solution 1: bruteforce
        # if len(s) == 1:
        #     return 1
        # longeststring = 0
        # for i in range(len(s)-1):
        #     currentstring = ''
        #     for j in range(i,len(s)):
        #         if s[j] not in currentstring:
        #             currentstring += s[j]
        #         else:
        #             break
        #         if len(currentstring) > longeststring:
        #             longeststring = len(currentstring)
        # return longeststring
        
        # solution 2: sliding window
        seen = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            if s[end] in seen: #if we have already seen the character
                start = max(start, seen[s[end]] + 1) #if we have seen the number, move the start to position after the last occurrence
                
            #updating last seen value of character
            seen[s[end]] = end
            max_length = max(max_length, end-start + 1)
        return max_length 
        