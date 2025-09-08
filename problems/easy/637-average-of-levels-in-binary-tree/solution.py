# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root.left and not root.right:
            return [root.val]

        tobevisited = [root]
        result = []
        while tobevisited:
            level = []
            len_lev = len(tobevisited)
            for _ in range(len_lev):
                node = tobevisited.pop(0)
                if node.left:
                    tobevisited.append(node.left)
                if node.right:
                    tobevisited.append(node.right)
                level.append(node.val)
            avg = sum(level)/len(level)
            result.append(avg)
        return result