# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        tobevisited = [root]
        l_2_r = True
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
            if l_2_r:
                result.append(level)
            else:
                result.append(level[::-1])
            l_2_r = not l_2_r
        return result        