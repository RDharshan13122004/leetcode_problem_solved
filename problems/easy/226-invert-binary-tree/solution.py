# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        q = [root]
        while q:
            visit = q.pop(0)
            visit.left,visit.right = visit.right,visit.left
            if visit.right:
                q.append(visit.right)
            if visit.left:
                q.append(visit.left)

        return root