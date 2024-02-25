class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        for i in range(len(haystack) - size + 1):
            if needle == haystack[i:i+size]:
                return i
        return -1