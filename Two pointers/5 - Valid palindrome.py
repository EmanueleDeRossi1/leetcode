"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        import re
        
        # remove all nun-alphanumeric characters (re.sub)
        # and convert into lowercase (lower()) 
        s_converted = re.sub("[^a-zA-Z\d]", "", s.lower())
        
        # invert the string
        s_converted_inverse = s_converted[::-1]
        
        # check if palindrome
        if s_converted == s_converted_inverse:
            return True
        else:
            return False
        
        
        return s_converted, s_converted_inverse
    
    

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(Solution().isPalindrome(s2))