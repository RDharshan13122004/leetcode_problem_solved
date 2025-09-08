# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = []
        tobevisited = [root]
        while tobevisited:
            level = []
            size_of = len(tobevisited)
            for _ in range(size_of):
                node = tobevisited.pop(0)
                level.append(node.val)
                if node.left:
                    tobevisited.append(node.left)
                if node.right:
                    tobevisited.append(node.right)
            result.append(level)
        return len(result)
        