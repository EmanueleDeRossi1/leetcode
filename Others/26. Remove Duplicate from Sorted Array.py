# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:38:47 2024

@author: emanu
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace_i = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace_i] = nums[i]
                replace_i += 1
        return replace_i
