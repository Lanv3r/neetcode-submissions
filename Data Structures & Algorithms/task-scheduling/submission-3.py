class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1
            if queue and queue[0][1] <= time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])
            if maxHeap:
                count = heapq.heappop_max(maxHeap) - 1
                if count > 0:
                    queue.append((count, time + n + 1))

        return time
