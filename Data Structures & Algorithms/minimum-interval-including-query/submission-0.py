class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        shortest_int = defaultdict(lambda: -1)
        for s, e in intervals:
            length = e - s + 1
            for n in range(s, e + 1):
                if shortest_int[n] == -1:
                    shortest_int[n] = length
                else:
                    shortest_int[n] = min(shortest_int[n], length)
        output = []
        for q in queries:
            output.append(shortest_int[q])
        return output