# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        tobevisited = [root]
        result = []
        while tobevisited:
            size = len(tobevisited)
            for i in range(size):
                node = tobevisited.pop(0)
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    tobevisited.append(node.left)
                if node.right:
                    tobevisited.append(node.right)
        return result