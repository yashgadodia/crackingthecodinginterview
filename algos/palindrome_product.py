# class Solution():
    
#     def palin(sefl,number):
#         if list(number) == list(number)[::-1]:
#             return True
#         return False
    
    
#     def largestPalindrome(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         palinarray = []
#         for i in range(n):
#             #check if palindrome
#             if palin(i):
#                 palinarray.append(i)
                
#         return max(palinarray)
            

class Solution(object):
    
    def largestPalindrome(self):
        """
        :type n: int
        :rtype: int
        """
        # palinarray = []
        # for i in range(n):
        #     #check if palindrome
        #     if str(i) == str(i)[::-1]:
        #         # print(i)
        #         palinarray.append(i)
                
        # return max(palinarray)%1337
        maximum = 0
        for i in range(n*9,999):
            for j in range(i,999):
                multiple = i*j
                if str(multiple) == str(multiple)[::-1]:
                    if multiple > maximum:
                        # print(multiple)
                        maximum = multiple

        print(maximum)
                    

                


l1 = Solution()
l1.largestPalindrome()
# l1.largestPalindrome(10)