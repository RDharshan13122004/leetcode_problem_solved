# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cam = 0

        def dfs(node):
            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 2 or right == 2:
                self.cam += 1
                return 0

            if left == 0 or right == 0:
                return 1

            return 2

        if dfs(root) == 2:
            self.cam += 1
        return self.cam