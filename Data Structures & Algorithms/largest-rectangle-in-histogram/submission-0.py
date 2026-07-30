class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0
        for i in range(len(heights)):
            cur_start = i
            while stack and heights[i] < stack[-1][0]:
                cur_start = stack[-1][1]
                res = max(res, stack[-1][0] * (i - stack[-1][1]))
                stack.pop()

            if not stack or heights[i] > stack[-1][0]:
                stack.append((heights[i], cur_start))
            res = max(res, stack[-1][0] * (i - stack[-1][1] + 1))
 
        i = n - 1
        while stack:
            res = max(res, stack[-1][0] * (i - stack[-1][1] + 1))
            stack.pop()

        return res
