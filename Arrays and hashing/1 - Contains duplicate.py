"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        already_there = set()

        for n in nums:
            if n in already_there:
                return True
            else:
                already_there.add(n)
            
        return False
            

            
nums1 = [1, 2, 3, 2]

print(Solution().containsDuplicate(nums1))