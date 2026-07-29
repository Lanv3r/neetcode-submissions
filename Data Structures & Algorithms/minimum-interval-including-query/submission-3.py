class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = []
        for i in range(len(queries)):
            sorted_queries.append((queries[i], i))
        sorted_queries.sort()
        output = [-1] * len(queries)

        k = 0
        heap = []
        for n, j in sorted_queries: 
            while k < len(intervals) and intervals[k][0] <= n:
                left, right = intervals[k][0], intervals[k][1]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                k += 1  
            while heap and heap[0][1] < n:
                heapq.heappop(heap)
            if heap:
                output[j] = heap[0][0]
        return output
