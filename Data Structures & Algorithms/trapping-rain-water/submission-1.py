class Solution:
    def trap(self, height: List[int]) -> int:
        def calc(l, r, total):
            if l >= r:
                return total
            if height[l] < height[r]:
                l_h = height[l]
                l += 1
                while l < r:
                    if height[l] >= l_h:
                        break
                    total += (l_h - height[l])
                    l += 1
                return calc(l, r, total)
            else:
                r_h = height[r]
                r -= 1
                while l < r:
                    if height[r] >= r_h:
                        break
                    total += (r_h - height[r])
                    r -= 1
                return calc(l, r, total)
        return calc(0, len(height) - 1, 0)    