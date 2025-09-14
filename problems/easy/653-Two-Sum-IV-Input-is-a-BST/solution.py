# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        tobevisited = [root]
        value = set()
        while tobevisited:
            node = tobevisited.pop(0)
            if k - node.val in value:
                return True
            value.add(node.val)
            if node.left:
                tobevisited.append(node.left)
            if node.right:
                tobevisited.append(node.right)
        else:
            return False