class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            middle = (left+right) // 2
            result = min(result, nums[middle])
            
            if nums[middle] >= nums[left]:
                left = middle + 1 
            else:
                right = middle - 1 
        return result
            
            
        


# mmmh you basically copied it from 
# https://www.youtube.com/watch?v=nIVW4P8b1VA&t=446s&ab_channel=NeetCode
nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]

print(Solution().findMin(nums2))