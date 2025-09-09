# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        self.pre(root,results)
        return results[k-1]
    def pre(self,node,res):
        if node:
            self.pre(node.left,res)
            res.append(node.val)
            self.pre(node.right,res)
