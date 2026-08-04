class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, total = 0, len(height) - 1, 0
        while l < r:
            if height[l] < height[r]:
                l_h = height[l]
                l += 1
                while l < r:
                    if height[l] >= l_h:
                        break
                    total += (l_h - height[l])
                    l += 1
            else:
                r_h = height[r]
                r -= 1
                while l < r:
                    if height[r] >= r_h:
                        break
                    total += (r_h - height[r])
                    r -= 1
        return total   