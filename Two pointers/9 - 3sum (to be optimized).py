"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""



## troppo lentooooooo

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # ordina nums
        nums.sort()
        
        solutions = []
        
        #i = 0
        #for i in range(len(nums)):
        
            
        # a + b + c = 0
        # is the same to a + b = -c
        
        
        for i in range(len(nums)-1):
            
            target = - (nums[i])
            j = 0
        
            while j < i and j != i:
                k = len(nums) - 1
                while k > j and k != j and k != i:
                    
                    #print("i", i, "j", j, "k", k)
                    if nums[k] + nums[j] == target:
                        sum_to_0 = sorted([nums[i], nums[j], nums[k]])
                        if sum_to_0 not in solutions:
                            solutions.append(sum_to_0) 
                    
                    k -= 1
                    
                    
                j += 1
                
                
        return solutions
            #print(j, k)
        
        



nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]


print(Solution().threeSum(nums1))
