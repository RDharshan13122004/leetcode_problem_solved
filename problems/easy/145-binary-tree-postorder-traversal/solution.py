# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder(root,result)
        return result

    def postorder(self,node,res):
        if node:
            self.postorder(node.left,res)
            self.postorder(node.right,res)
            res.append(node.val)