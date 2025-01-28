# -*- coding: utf-8 -*-
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


TIME LIMIT EXCEEDED :((


"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter

                
        # count number of times number appears
        count = Counter(nums)
                    
        # create a list of numbers from most frequent to least
        sorted_list = sorted(count, key = count.get, reverse = True)
        
        # get the k most frequent numbers
        k_most_frequent = sorted_list[:k]
        
                
        return k_most_frequent
            
        # sort count_dict() with sorted method
        
        #sorted_list = sorted(count_dict, key = count_dict.get, reverse = True)
            
        #k_most_frequent = sorted_list[:k]
        
        #return k_most_frequent
                    
        # sort the dictionary with sorted() method
        # use the items() method on the dictionary to retrieve its keys and values
        # lambda function to get the values retrieved with the item() method
        # reverse to put highest values at the beginning

        # sorted_dict = sorted(count_dict.items(), key=lambda x:x[1], reverse = True)
        
        # for i in range(k):
        #     k_most_frequent.append(sorted_dict[0][0])
        #     sorted_dict.pop(0)
        
        # return k_most_frequent
        
        
        # # create a dict to store the number of times the number appears
        # count_dict = dict()
        # for num in nums:
        #     count_dict[num] = nums.count(num)
            
            
        # # create a list of len(k) to store most frequent numbers
        # frequent = list()
        
        # for i in range(k):
        #     #print(count_dict)
        #     if len(count_dict) > 0:
        #         highest_number = max(count_dict.values())
        #         for number in count_dict.copy():
        #             if count_dict[number] == highest_number:
        #                 frequent.append(number)
        #                 count_dict.pop(number)
        # return frequent
        

nums1 = [1,1,1,2,4,4,4,4,4,4]
k1 = 2

nums2 = [1]
k2 = 1

nums3 = [5,6]
k3 = 2

nums4 = [4,1,-1,2,-1,2,3]

k4 = 2

nums5 = [2, 3, 5, 2, 2, 6, 6, 2, 6]
k5 = 2

nums6 = [4,1,7,2,7,2,3]
k6 = 2

#dizionario = {1:10, 2: 15, 3:20, 4:20, 5:30, 7: 5}

#dizionario.pop(1)

#sortao = sorted(dizionario.items(), key = lambda x:x[1], reverse = True)


#print(sortao)

print(Solution().topKFrequent(nums6, k6))

