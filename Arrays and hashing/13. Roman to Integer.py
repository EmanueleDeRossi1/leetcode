# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:35:57 2024

@author: emanu
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        previous = 0
        for letter in reversed(s):
            current = roman_numerals[letter]
            if previous > current:
                total -= current
            else:
                total += current
            previous = current
        return total
