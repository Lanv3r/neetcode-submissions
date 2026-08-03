class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 0
        while n > 0: 
            count += 1
            bit = n & 1
            if bit == 1:
                res += 2 ** (32 - count)
            n = n >> 1
        return res