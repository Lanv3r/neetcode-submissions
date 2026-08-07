class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        
        for n in nums:
            next_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    if copy not in next_perms:
                        next_perms.append(copy)
            perms = next_perms
        return perms