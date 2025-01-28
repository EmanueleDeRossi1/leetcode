"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = []
        counters = []
        
        from collections import Counter
        
        for word in strs:
            count = Counter(word)
            if count not in counters:
                counters.append(count)
                groups.append([word])
            else:
                groups[counters.index(count)].append(word)
        return groups
        
    
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(Solution().groupAnagrams(strs1))