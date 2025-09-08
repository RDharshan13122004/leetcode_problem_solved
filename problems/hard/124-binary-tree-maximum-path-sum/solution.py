# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')
        self.dfs(root)
        return self.max_val
    def dfs(self,node):
        if not node:
            return 0
        
        left_gain = max(self.dfs(node.left),0)
        right_gain = max(self.dfs(node.right),0)

        current_sum = node.val + left_gain + right_gain

        self.max_val = max(self.max_val,current_sum)
        return node.val + max(left_gain,right_gain)