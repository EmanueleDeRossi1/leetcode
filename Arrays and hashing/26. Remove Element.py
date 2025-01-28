# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:38:47 2024

@author: emanu
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1

        return i 
