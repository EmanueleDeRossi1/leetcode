# this is not binary search though lol

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1
        
nums1 = [4,5,6,7,0,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [1]

target1 = 0
target2 = 3
target3 = 0

print(Solution().search(nums1, target1))