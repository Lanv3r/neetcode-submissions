class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = []
        for i in range(len(queries)):
            sorted_queries.append((queries[i], i))
        sorted_queries.sort()
        output = [-1] * len(queries)

        for q, i in sorted_queries:
            heap = []
            k = 0
            while k < len(intervals) and intervals[k][0] <= q:
                length = intervals[k][1] - intervals[k][0] + 1
                heapq.heappush(heap, (length, intervals[k][1]))
                k += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                output[i] = heap[0][0] 

        return output
