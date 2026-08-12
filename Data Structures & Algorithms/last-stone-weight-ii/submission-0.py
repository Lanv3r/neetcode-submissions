class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        cache = [0] * (target + 1)
        for s in stones:
            cur = [0] * (target + 1)
            for i in range(1, target + 1):
                skip = cache[i]
                include = 0
                if i - s >= 0:
                    include = cache[i-s] + s
                cur[i] = max(skip, include)
            cache = cur
        return abs(total - 2 * cache[target])

