"""

Given a string s, find the length of the longest 
substring
 without repeating characters.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # build a sliding window, composed on a start pointer at the beginning
        # of the window and a end pointer at the end
        
        
        start_pointer = 0
        max_window = ""
        # loop though end_pointer
        for end_pointer in range(1, len(s)+1):
            window = s[start_pointer:end_pointer]
            #print(window, start_pointer, end_pointer)
            
            # if window has duplicates
            if len(window) != len(set(window)):
                
                # if there are duplicates while moving the end-point, that means that the last 
                # character is already in the window somewhere. Find the index of the other character inside the window, 
                # so you can move the start point up to the position after that character
                idx_double_char = [window.index(k) for k in window[:-1] if k == window[-1]]
                start_pointer = start_pointer + idx_double_char[0] + 1 
        
            # window has no duplicates
            if len(window) == len(set(window)):
               
                # if the lenght of our window is bigger that our max_window yet, set it to max_window
                if len(window) > len(max_window):
                    max_window = window
        return len(max_window)
                
        
    


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = ""
s5 = "dvdf"
s6 = "bbtablud"
s7 = "aab"

print(Solution().lengthOfLongestSubstring(s2))