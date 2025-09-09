# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        tobevisited = [root]
        while tobevisited:
            level = []
            level_size = len(tobevisited)
            for _ in range(level_size):
                node = tobevisited.pop(0)
                level.append(node.val)
                if node.left:
                    tobevisited.append(node.left)
                if node.right:
                    tobevisited.append(node.right)
            result.append(level)
        return result

        