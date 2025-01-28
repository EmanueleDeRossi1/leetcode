class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = {}
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1

        for idx, char in enumerate(s):
            if char_counts[char] == 1:
                return idx
        return -1