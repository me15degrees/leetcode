class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2): 
            sbstr = s[i:i+3] 
            if len(set(sbstr)) == len(sbstr):  
                count += 1
        return count