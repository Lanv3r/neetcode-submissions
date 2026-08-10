class Solution:
    def getSum(self, a: int, b: int) -> int:
        for _ in range(32):
            if not b:
                break
            a, b = a ^ b, (a & b) << 1
        mask = 0xFFFFFFFF
        if b:
            return a & mask
        return a 