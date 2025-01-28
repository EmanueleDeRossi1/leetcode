"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_count_s = dict()
        char_count_t = dict()
        
        # store char count of s in dictionary
        for char in s:
            if char not in char_count_s:
                char_count_s[char] = 1
            else:
                char_count_s[char] += 1
                
        # do the same thing for t
        for char in t:
            if char not in char_count_t:
                char_count_t[char] = 1
            else:
                char_count_t[char] += 1
        
        # if the dictionaries are the same, return true, else false
        if char_count_s == char_count_t:
            return True
        else:
            return False
    
            
    
        

                
        # for character in s:
        #     if character not in t or len(t) != len(s):
        #         return False
        
        # return True
        # chatgpt uses sort

        
s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"

print(Solution().isAnagram(s1, t1))
print(Solution().isAnagram(s2, t2))

# string = "vediamo"
# string_inverted = string[::-1]

        # lista = []
        # if len(t) == len(s):
        #     for character in s:
        #         if character not in t:
        #              lista.append(False)
        #         else:
        #             lista.append(True)
            
        #     if False in lista:
        #         return False
        #     else:
        #         return True
        # else:
        #     return False

