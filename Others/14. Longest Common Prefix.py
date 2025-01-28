class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return longest
            longest += char
        return longest
        