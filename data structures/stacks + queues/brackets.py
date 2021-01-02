'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

'''

# approach 

# 1) Initialize a stack S.
# Process each bracket of the expression one at a time.
# 2) If we encounter an opening bracket, we simply push 
# it onto the stack. This means we will process it 
# later, let us simply move onto the sub-expression ahead.
# 3) If we encounter a closing bracket, then we check the 
# element on top of the stack. If the element at the top 
# of the stack is an opening bracket of the same type,
#  then we pop it off the stack and continue processing.
#   Else, this implies an invalid expression.
# 5) In the end, if we are left with a stack still having 
# elements, then this implies an invalid expression.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        mapping = {")":"(","}":"{","]":"["}

        for ch in s:
            if ch in mapping: #closing bracket
                # print(ch)
                topelement = stack.pop() if stack else "#"
                if mapping[ch] != topelement:
                    return False
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return not stack


        # opening = {"(":1,"[":2,"{":3} #give arbitrary key, same as matching, value is bracket
        # closing = {")":1,"]":2,"}":3}
        # mystack = [] #initialise stack

        # for bracket in s:
        #     if bracket in opening:
        #         # print(bracket)
        #         mystack.append(bracket) #push to stack
        #     if bracket in closing:
        #         # print(closing[bracket])
        #         # print(opening[mystack[-1]])
        #         if len(mystack) > 0:
        #             # print(closing[bracket])
        #             if closing[bracket] == opening[mystack[-1]]: #check if matches
        #                 # print(mystack)
        #                 mystack = mystack[:-1]
        #                 # print(mystack)
        #             else:
        #                 return False
        #         else:
        #             return False

        # # print(mystack)
        # if len(mystack) > 0:
        #     return False
        # if len(s) == 1:
        #     return False
        # return True



        
s1 = Solution()
print(s1.isValid("[])"))

