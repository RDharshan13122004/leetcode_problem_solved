# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tobevisited = [(root,1)]
        while tobevisited:
            node, depth = tobevisited.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                tobevisited.append((node.left, depth + 1))          
            if node.right:
                tobevisited.append((node.right, depth + 1))