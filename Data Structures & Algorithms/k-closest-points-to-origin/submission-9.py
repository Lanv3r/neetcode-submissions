class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, right = 0, len(points) - 1
        while left <= right:
            pivot_dist = points[right][0] ** 2 + points[right][1] ** 2
            l = left
            for i in range(left, right):
                cur_dist = points[i][0] ** 2 + points[i][1] ** 2
                if cur_dist < pivot_dist:
                    points[l], points[i] = points[i], points[l]
                    l += 1
            points[l], points[right] = points[right], points[l]
            if l == k or l == k - 1:
                return points[:k]
            elif l < k - 1:
                left = l + 1    
            else:
                right = l - 1
        return points[:k]

