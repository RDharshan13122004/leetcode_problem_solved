# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        tobevisited = [root]
        while tobevisited:
            node = tobevisited.pop(0)
            if low <= node.val and node.val <= high:
                total += node.val
            if node.left:
                tobevisited.append(node.left)
            if node.right:
                tobevisited.append(node.right)
        return total