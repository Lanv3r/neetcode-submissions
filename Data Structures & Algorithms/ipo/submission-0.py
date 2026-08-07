class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        count = 0
        cap = w
        minheap = []
        for i in range(len(profits)):
            heapq.heappush(minheap, (capital[i], profits[i]))
        maxheap = []
        while count < k:
            while minheap and minheap[0][0] <= cap:
                c, p = heapq.heappop(minheap)
                heapq.heappush_max(maxheap, p)
            if not maxheap:
                return cap
            cap += heapq.heappop_max(maxheap)
            count += 1
        return cap