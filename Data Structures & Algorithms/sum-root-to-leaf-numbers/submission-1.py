# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if node is None:
                return 0 
            if node.left is None and node.right is None:
                return current_sum * 10 + node.val
            return dfs(node.right, current_sum * 10 + node.val) + dfs(node.left, current_sum * 10 + node.val)

        return dfs(root, 0)