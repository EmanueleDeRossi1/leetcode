# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:38:46 2024

@author: emanu
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # This works in n*m time

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:                
                return i
        return -1
           
        # Try doing it with the KMP algorithm?