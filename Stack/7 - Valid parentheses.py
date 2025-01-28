"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        open_pars = ["(", "[", "{"]
        closed_pars = [")", "]", "}"]
        
        stack = list()
        
        for char in s:
            if char in open_pars:
                stack.append(char)
            if char in closed_pars:
                # if char is the closing char of the open char on top of the stack
                if stack!= [] and char == closed_pars[open_pars.index(stack[-1])]:
                    stack.pop()
                    print("aaa")
                else:
                    return False
                
                
        return True if stack == [] else False
    
    

s1 = "()"
s2 = "()[]{}" 
s3 = "(]"
s4 = "[()]"
s5 = "]"


print(Solution().isValid(s5))