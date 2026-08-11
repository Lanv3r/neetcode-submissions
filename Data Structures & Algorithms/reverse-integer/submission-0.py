class Solution:
    def reverse(self, x: int) -> int:
        total = 0
        a = abs(x)
        while a > 0:
            total = (total * 10) + (a % 10)
            a = a // 10
        if x < 0:
            total = -total
        if total < -2 ** 31 or total > 2 ** 31 - 1:
            return 0
        return total
