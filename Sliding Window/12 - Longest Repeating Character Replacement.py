class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        start_pointer = 0
        end_pointer = 0
        max_window = ""
        char_count = {}
        
                
        for end_pointer in range(0, len(s)):
            window = s[start_pointer:end_pointer+1]
            char_count[s[end_pointer]] = 1 + char_count.get(s[end_pointer], 0)
            number_of_all_values_to_replace = sum(char_count.values()) - max(char_count.values())
            #print(window, max_window, char_count)
            if number_of_all_values_to_replace > k:
                char_count[s[start_pointer]] -= 1
                start_pointer += 1
            elif len(window) > len(max_window):
                max_window = window
        return max_window
                
            
        #return max_window
        #     if char_count:
        #         most_frequent_char = max(char_count, key=lambda k: char_count[k])
        #         char_count_without_most_frequent =  {k:v for k,v in char_count.items() if k != most_frequent_char}
                
        #         if char_count_without_most_frequent:
        #             if max(char_count_without_most_frequent.values()) < k:
        #                 max_window == window
        #                 print("char_count_without_most_frequent", char_count_without_most_frequent, "bb", max(char_count_without_most_frequent, key=lambda k: char_count_without_most_frequent[k]))
                        
        #             else:
        #                 # change start_pointer
        #                 start_pointer = window.find(max(char_count_without_most_frequent, key=lambda k: char_count_without_most_frequent[k]), 0, len(window))
                        
        # return max_window
                # if sum(char_count_without_most_frequent.values()) <= k:
                #     print("minoreee o uguale")
                    
s1 = "ABABB"
k1 = 2
s2 = "AABABBA"
k2 = 1
s3 = "ABAA"
k3 = 0
s4 = "ABBB"
k4 = 2
s5 = "AABABBA"
k5 = 1
s6 = "EQQEJDOBDPDPFPEIAQLQGDNIRDDGEHJIORMJPKGPLCPDFMIGHJNIIRSDSBRNJNROBALNSHCRFBASTLRMENCCIBJLGAITBFCSMPRO"
k6 = 2
s7 = "BAAA"
k7 = 0


print(Solution().characterReplacement(s6, k6))