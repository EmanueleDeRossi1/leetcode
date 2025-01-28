"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_product = [1] * (len(nums)+1)
        right_product = [1] * (len(nums)+1)
        answer = [1] * len(nums)
        
        #print(nums)
        for i in range(0, len(nums)):
           right_product[i] = right_product[i-1] * nums[i]
           #print("ir", i)
           
        for i in reversed(range(len(nums))):
            left_product[i] = left_product[i+1] * nums[i]
            print("il", i)
            
        for i in range(0, len(nums)):
            answer[i] = right_product[i-1] * left_product[i+1]
        #print(answer)
        return answer
    

nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
nums3 = [1, 5, 2, 3]
nums4 = [3, 2, 5, 1]


print(Solution().productExceptSelf(nums2))


# lista = [1,2,3,4,5,6]

# import numpy

# lista_senza_5 = lista[:4] + lista[4+1:]

# print(numpy.prod(lista_senza_5))

# print(lista_senza_4)