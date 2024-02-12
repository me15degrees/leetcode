class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        nice_strings = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):  
                substring = s[i:j]
                if all(char.swapcase() in substring for char in substring): 
                    nice_strings.append(substring)
        if nice_strings:  
            return max(nice_strings, key=len) 
        else:
            return "" 