class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # #solution 1: bruteforce
        if len(s) == 1:
            return 1
        longeststring = 0
        for i in range(len(s)-1):
            currentstring = ''
            for j in range(i,len(s)):
                if s[j] not in currentstring:
                    currentstring += s[j]
                else:
                    break
                if len(currentstring) > longeststring:
                    longeststring = len(currentstring)
        return longeststring