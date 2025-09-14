# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        tobevisited = [root]
        res = []
        while tobevisited:
            level = []
            size = len(tobevisited)
            for _ in range(size):
                node = tobevisited.pop(0)
                if node.left:
                    tobevisited.append(node.left)
                if node.right:
                    tobevisited.append(node.right)
                level.append(node.val)
            res.append(max(level))
        return res