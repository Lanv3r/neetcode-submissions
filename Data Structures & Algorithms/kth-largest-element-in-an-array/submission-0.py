class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        while k > 0:
            cur = heapq.heappop_max(heap)
            k -= 1
        return cur