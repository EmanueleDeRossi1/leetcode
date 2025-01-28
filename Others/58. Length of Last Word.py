# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:38:44 2024

@author: emanu
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_last = 0
        for i in range(len(s)):
            if s[i] != " ":
                len_last += 1
            if s[i-1] == " " and s[i] != " ":
                len_last = 1

        return len_last