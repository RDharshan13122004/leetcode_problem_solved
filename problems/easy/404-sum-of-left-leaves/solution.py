# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        sums = 0
        tobevisited = [root]
        while tobevisited:
            node = tobevisited.pop(0)
            if node.left:
                tobevisited.append(node.left)
                if node.left and not node.left.left and not node.left.right:
                    sums += node.left.val
            if node.right:
                tobevisited.append(node.right)
        return sums