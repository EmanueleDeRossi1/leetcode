# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:40:47 2024

@author: emanu
"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove all nun-alphanumeric characters (re.sub)
        # and convert into lowercase (lower()) 
        s_converted = re.sub("[^a-zA-Z\d]", "", s.lower())

        i = 0
        j = len(s_converted) -1


        while i<j:
            if s_converted[i] != s_converted[j]:
                return False
            i += 1
            j -= 1
        return True
