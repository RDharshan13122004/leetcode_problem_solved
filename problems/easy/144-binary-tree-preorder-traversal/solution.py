# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorder(root,result)
        return result

    def preorder(self,node,res):
        if node:
            res.append(node.val)
            self.preorder(node.left,res)
            self.preorder(node.right,res)