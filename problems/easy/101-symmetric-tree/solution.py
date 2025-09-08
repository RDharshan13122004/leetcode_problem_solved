# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        tobevisited = [root]
        while tobevisited:
            level = []
            for node in tobevisited:
                if node:
                    level.append(node.left)
                    level.append(node.right)

            value = [node.val if node else None for node in level]

            if value != value[::-1]:
                return False

            tobevisited = level

        return True
