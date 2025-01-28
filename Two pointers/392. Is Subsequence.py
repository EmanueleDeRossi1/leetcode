class Solution: 
   def isSubsequence(self, s: str, t: str) -
       i = 0 
       if len(s) == 0: 
           return True 
       for j in range(len(t)): 
           if s[i] == t[j]: 
               i += 1 
           if len(s) == i: 
               return True 
