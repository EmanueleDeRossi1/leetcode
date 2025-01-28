"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if n1 + n2 == target and i1 != i2:
                    return i1, i2

class Solution(object):
    def twoSum_optimized(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

nums1 = [2,7,11,15]
target1 = 9
# Output: [0,1]

nums2  = [3,2,4]
target2 = 6
# Output: [1,2]

nums3 = [3,3]
target3 = 6
# Output: [0,1]

#print(Solution().twoSum(nums3, target3))
print(Solution().twoSum_optimized(nums3, target3))