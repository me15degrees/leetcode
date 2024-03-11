class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        while n > -1:
            temp = n
            count = 0
            while temp:
                count += temp & 1
                temp = temp >> 1
            res.append(count)
            n -= 1
        return res[::-1]